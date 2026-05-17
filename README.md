# Olist Logistics Pipeline - Microsoft Fabric & Python

## 📊 Resumo do Projeto
Pipeline de Engenharia de Dados desenvolvido para analisar o **Lead Time** e a satisfação do cliente no marketplace Olist. O projeto utiliza uma arquitetura híbrida para contornar limitações de instabilidade em nuvem, processando dados pesados localmente e servindo os insights no Microsoft Fabric.

## 🏗️ Arquitetura Medallion
- **Bronze**: Dados brutos extraídos do dataset público da Olist.
- **Silver**: Limpeza, tipagem de datas e normalização via Python (Pandas).
- **Gold**: Agregação de KPIs de atraso por estado e identificação de vendedores ofensores.

## 🛠️ Stack Técnica
- **Linguagem**: Python 3.x
- **Ambiente**: CachyOS (Linux) / Microsoft Fabric
- **Principais Ferramentas**: Pandas, Power BI Desktop, Git.

## 📈 Resultados
O dashboard final (disponível na pasta `/gold` e no Power BI) identifica que a taxa de atraso impacta diretamente o `review_score`, permitindo ações direcionadas nos estados de maior gargalo.
