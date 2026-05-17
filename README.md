# Olist Logistics Analytics - Microsoft Fabric & Python

## 📌 Sobre o Projeto
Este projeto simula um pipeline de dados corporativo para análise de performance logística do marketplace **Olist**. O objetivo é identificar gargalos de entrega, performance de vendedores por estado e o impacto do atraso na satisfação do cliente.

## 🏗️ Arquitetura do Projeto
O projeto segue a arquitetura **Medallion** (Bronze, Silver, Gold), adaptada para um fluxo híbrido:
1. **Bronze**: Dados brutos em CSV (Ingestão).
2. **Silver**: Processamento local em Python (Pandas/CachyOS) para limpeza, tipagem de datas e Joins complexos.
3. **Gold**: Geração de KPIs agregados de logística e produtividade de vendedores.
4. **Power BI**: Visualização final dos insights.

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.10+
- **Bibliotecas**: Pandas, NumPy
- **Infraestrutura**: Microsoft Fabric (Lakehouse)
- **Visualização**: Power BI
- **Sistema Operacional**: CachyOS (Arch Linux)

## 📊 Principais Insights Gerados
- **Taxa de Atraso Global**: Identificação do % de pedidos fora do SLA.
- **Lead Time por Estado**: Média de dias que cada estado leva para receber um produto.
- **Top Vendedores Ofensores**: Ranking de vendedores com maior índice de atraso e baixa nota de review.

## 🚀 Como Executar
1. Clone o repositório.
2. Certifique-se de ter os dados da Olist na pasta `/bronze`.
3. Execute `python scripts/etl_silver.py`.
4. Execute `python scripts/etl_gold.py`.
