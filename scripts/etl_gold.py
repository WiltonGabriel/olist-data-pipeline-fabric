import pandas as pd
import numpy as np

print("Iniciando processamento da Camada Ouro (Gold)...")

path_silver = "../silver/"
path_gold = "../gold/"

# 1. Carregando a base limpa (Prata)
print("Lendo a Tabela Fato da Camada Silver...")
df_master = pd.read_csv(path_silver + "silver_logistica_master.csv")
df_customers = pd.read_csv(path_silver + "silver_customers.csv")

# Trazendo a sigla do estado do cliente para a tabela master
df_master = pd.merge(df_master, df_customers[['customer_id', 'customer_state']], on="customer_id", how="left")

print("Calculando KPIs de Negócio...")

# KPI 1: Resumo de Logística por Estado (Mapa do Brasil)
# Descobre a média de dias de trânsito e o total de pedidos atrasados por Estado
gold_estado = df_master.groupby('customer_state').agg(
    total_pedidos=('order_id', 'count'),
    media_dias_transito=('tempo_transito_dias', 'mean'),
    pedidos_com_atraso=('teve_atraso', 'sum')
).reset_index()

# Calcula a porcentagem de atraso (% SLA Quebrado)
gold_estado['taxa_atraso_perc'] = round((gold_estado['pedidos_com_atraso'] / gold_estado['total_pedidos']) * 100, 2)
gold_estado['media_dias_transito'] = round(gold_estado['media_dias_transito'], 1)

# KPI 2: Ranking de Vendedores Ofensores (Os piores da plataforma)
# Vendedores que têm mais de 50 vendas e a maior taxa de atraso
gold_vendedores = df_master.groupby('seller_id').agg(
    total_vendas=('order_id', 'count'),
    pedidos_atrasados=('teve_atraso', 'sum'),
    media_nota_cliente=('review_score', 'mean')
).reset_index()

# Filtra só quem vendeu um volume razoável (mais de 50) e ordena pelos piores
ofensores = gold_vendedores[gold_vendedores['total_vendas'] > 50].copy()
ofensores['taxa_atraso_perc'] = round((ofensores['pedidos_atrasados'] / ofensores['total_vendas']) * 100, 2)
ofensores['media_nota_cliente'] = round(ofensores['media_nota_cliente'], 2)
gold_vendedores_top_piores = ofensores.sort_values(by='taxa_atraso_perc', ascending=False)

print("Salvando as Tabelas da Camada Ouro...")
gold_estado.to_csv(path_gold + "gold_kpi_estado.csv", index=False)
gold_vendedores_top_piores.to_csv(path_gold + "gold_kpi_vendedores_ofensores.csv", index=False)

print("SUCESSO! Arquivos Gold gerados na pasta /gold/")
