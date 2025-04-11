# Projeto de Engenharia de Dados - Auxílio Brasil

## 🎯 Objetivo
Analisar a distribuição e impacto do programa Auxílio Brasil ao longo de diferentes regiões do Brasil.

### Perguntas de negócio:
1. Qual foi o valor total distribuído por estado?
2. Qual foi o ticket médio por beneficiário?
3. Quais os estados com maior número de beneficiários?
4. Existe correlação entre o valor recebido e a população local?

## 🔍 Coleta
Utilizamos o dataset `202301_AuxilioBrasil.csv`, obtido do GitHub:
https://github.com/tleal92/engenharia-dados-clima-rj

O script de coleta está em `scripts/download_auxilio_brasil.py`.

## 🧱 Modelagem
O modelo utilizado é um esquema flat (Data Lake). O catálogo completo está em `catalogo_dados.csv`.

## ⚙️ Carga
Os dados foram carregados para o Databricks Community Edition, via upload manual.

## 📊 Análise
A análise foi realizada com SQL no Databricks. As evidências estão no notebook e em capturas de tela.

## ✅ Autoavaliação
O projeto atinge os objetivos propostos, com pipeline completo: coleta, modelagem, carga e análise.
