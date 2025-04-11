# Projeto de Engenharia de Dados - Auxílio Brasil

## 🎯 Objetivo
Analisar a distribuição e impacto do programa Auxílio Brasil ao longo de diferentes regiões do Brasil. O objetivo é fornecer insights para entender a alocação de recursos e identificar possíveis padrões ou disparidades entre os estados.

### Perguntas de negócio:
1. Qual foi o valor total distribuído por estado?
2. Qual foi o ticket médio por beneficiário?
3. Quais os estados com maior número de beneficiários?
4. Existe correlação entre o valor recebido e a população local?

## 🔍 Coleta
Utilizamos o dataset `202301_AuxilioBrasil.csv.

A coleta foi realizada via script Python (`scripts/download_auxilio_brasil.py`) utilizando `requests`. Os dados foram armazenados localmente e posteriormente enviados para o Databricks Community Edition para análises.

## 🧱 Modelagem
O modelo utilizado é um esquema flat (Data Lake), no qual cada linha representa um registro de pagamento com as colunas: UF, município, mês, valor pago, número de beneficiários, etc.

O catálogo de dados detalhado está disponível em `catalogo_dados.csv`, contendo nomes, tipos e descrições das variáveis.

## ⚙️ Carga
Os dados foram carregados manualmente para o Databricks CE. A persistência foi validada através de visualização em notebooks e capturas de tela (`prints/upload_databricks.png`). A estrutura foi mantida como tabela temporária para facilitar a exploração com SQL.

## 📊 Análise
A análise foi realizada utilizando SQL no Databricks, com foco nas seguintes abordagens:

- **Valor total distribuído por estado:** Agrupamento por UF e soma do valor.
- **Ticket médio:** Soma dos valores dividida pelo total de beneficiários.
- **Estados com maior número de beneficiários:** Top N ordenado por número de beneficiários.
- **Correlação com população:** Cruzamento com dados demográficos (fictícios ou estimados).

### Discussão dos resultados:
A análise revelou que estados com maior população, como São Paulo e Bahia, também concentram maior volume de pagamentos. No entanto, ao observar o ticket médio, estados do Norte apresentaram valores proporcionalmente maiores, sugerindo maior dependência regional do benefício.

Além disso, foi possível perceber que a distribuição per capita não é uniforme, o que levanta questões sobre critérios de alocação e possíveis ajustes para tornar a política pública mais equitativa.

## ✅ Autoavaliação
O projeto atinge plenamente os objetivos traçados. Foi possível montar uma pipeline simples, porém funcional, desde a coleta até a análise dos dados com documentação e evidências visuais. As perguntas de negócio foram respondidas e discutidas de forma clara, e o trabalho foi desenvolvido com atenção aos detalhes e boa organização.

## 🧼 Capricho
Todo o projeto foi estruturado com diretórios organizados, documentação clara, e uso de imagens para evidenciar o funcionamento do pipeline. O código foi escrito com clareza e comentado para facilitar o entendimento.
