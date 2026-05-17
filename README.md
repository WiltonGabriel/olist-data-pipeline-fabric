# Pipeline de Engenharia de Dados: Olist Logistics Analytics

## 📌 Visão Geral
Este repositório contém a solução completa de engenharia de dados desenvolvida para analisar a operação logística do marketplace **Olist**. O objetivo principal do projeto foi transformar dados brutos em insights estratégicos sobre o tempo de entrega (Lead Time), performance de vendedores e o impacto direto da logística na satisfação do consumidor final.

Implementamos uma **Arquitetura Medallion** (Medalhão) para garantir a governança, limpeza e a qualidade dos dados em cada etapa do processo, permitindo uma análise confiável e escalável.

---

## 🏗️ Arquitetura e Fluxo de Dados
Desenvolvemos uma arquitetura híbrida para otimizar o processamento. O tratamento pesado dos dados foi realizado em ambiente local (CachyOS/Linux) para garantir performance, com a persistência e consumo final centralizados no **Microsoft Fabric**.

```mermaid
graph LR
    subgraph "Camada de Origem"
        A[Datasets CSV - Olist] -- Ingestão --> B{Pipeline Python}
    end

    subgraph "Microsoft Fabric (OneLake)"
        B --> C[(Camada Bronze)]
        C -- Refinamento --> D[(Camada Silver)]
        D -- Agregação --> E[(Camada Gold)]
    end

    subgraph "Camada de Entrega"
        E --> F[Dashboard Power BI]
    end

    style C fill:#cd7f32,stroke:#333,stroke-width:2px
    style D fill:#c0c0c0,stroke:#333,stroke-width:2px
    style E fill:#ffd700,stroke:#333,stroke-width:2px

```

---

## 🗂️ Detalhamento das Camadas

### 1. Camada Bronze (Raw)

Nesta etapa, realizamos a ingestão dos dados brutos sem modificações. O objetivo é manter uma cópia fiel da origem no OneLake, servindo como nossa "fonte da verdade" para qualquer necessidade de reprocessamento ou auditoria.

### 2. Camada Silver (Cleansed)

Aqui aplicamos as regras de limpeza e padronização. Utilizamos Python e Pandas para:

* **Tipagem de Dados:** Conversão de strings para formatos de data (datetime) e numéricos.
* **Tratamento de Nulos:** Tratamento de valores ausentes em colunas críticas de logística.
* **Modelagem Fato-Dimensão:** Cruzamento de múltiplos datasets (pedidos, itens, pagamentos e reviews) para gerar uma visão unificada da operação.

### 3. Camada Gold (Curated)

A camada final contém os dados prontos para o negócio. Criamos agregações focadas em KPIs (Indicadores Chave de Desempenho), reduzindo a complexidade para a ferramenta de BI:

* **Análise de SLA:** Cálculo de atrasos reais versus prazos prometidos.
* **Performance por Estado:** Média de tempo de trânsito por região do Brasil.
* **Ranking de Ofensores:** Identificação de vendedores com alta taxa de atraso e baixo índice de satisfação.

---

## 🛠️ Stack Tecnológica

* **Linguagem Principal:** Python 3.x (Pandas e NumPy).
* **Ambiente de Dados:** Microsoft Fabric (Lakehouse e OneLake).
* **Business Intelligence:** Power BI Desktop / Service.

---

## 📊 Resultados e Insights

O pipeline processou com sucesso toda a base histórica da Olist, revelando gargalos logísticos críticos. Identificamos uma **taxa média de atraso de 6,64%**, com variações regionais significativas que impactam diretamente o *Review Score* dos vendedores. O projeto agora serve como base para tomadas de decisão sobre parcerias logísticas e gestão de vendedores na plataforma.
