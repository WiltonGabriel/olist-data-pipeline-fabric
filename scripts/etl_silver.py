import pandas as pd

print("Iniciando Pipeline de Dados (CachyOS Local)...")
path_bronze = "../bronze/"
path_silver = "../silver/"

print("1. Lendo os arquivos da Camada Bronze...")
df_orders = pd.read_csv(path_bronze + "olist_orders_dataset.csv")
df_items = pd.read_csv(path_bronze + "olist_order_items_dataset.csv")
df_sellers = pd.read_csv(path_bronze + "olist_sellers_dataset.csv")
df_reviews = pd.read_csv(path_bronze + "olist_order_reviews_dataset.csv") # Pegando as notas dos clientes!

print("2. Tratando as datas...")
colunas_data = ['order_purchase_timestamp', 'order_delivered_carrier_date', 
                'order_delivered_customer_date', 'order_estimated_delivery_date']

for col in colunas_data:
    df_orders[col] = pd.to_datetime(df_orders[col])

print("3. Cruzando as tabelas vitais para Logística e Satisfação...")
# Junta Pedidos + Itens + Vendedores + Avaliações
df_join1 = pd.merge(df_orders, df_items, on="order_id", how="inner")
df_join2 = pd.merge(df_join1, df_sellers, on="seller_id", how="inner")
df_master = pd.merge(df_join2, df_reviews[['order_id', 'review_score']], on="order_id", how="left")

print("4. Calculando as métricas de negócio (Tempos e Atrasos)...")
df_master['tempo_separacao_dias'] = (df_master['order_delivered_carrier_date'] - df_master['order_purchase_timestamp']).dt.days
df_master['tempo_transito_dias'] = (df_master['order_delivered_customer_date'] - df_master['order_delivered_carrier_date']).dt.days
df_master['dias_atraso'] = (df_master['order_delivered_customer_date'] - df_master['order_estimated_delivery_date']).dt.days

# Cria uma coluna dizendo se atrasou ou não (Verdadeiro/Falso)
df_master['teve_atraso'] = df_master['dias_atraso'] > 0

print("5. Salvando resultado final na Camada Silver...")
# Esse CSV final é o que você vai mandar para o Fabric
df_master.to_csv(path_silver + "silver_logistica_master.csv", index=False)

# (Opcional) Copiando a tabela de Clientes limpa para a Silver para o PBI usar depois
df_customers = pd.read_csv(path_bronze + "olist_customers_dataset.csv")
df_customers.to_csv(path_silver + "silver_customers.csv", index=False)

print("SUCESSO! A tabela Master e a tabela de Clientes foram geradas na pasta Silver.")
