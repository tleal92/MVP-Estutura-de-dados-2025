# Projeto MVP - Engenharia de Dados - Bank Marketing

Este repositório contém o projeto final do MVP da disciplina de Engenharia de Dados, utilizando o dataset **Bank Marketing** da UCI Machine Learning Repository.

## 🔍 Objetivo

O objetivo deste projeto é analisar os dados de campanhas de marketing de um banco português e entender **quais fatores influenciam a adesão ao produto de depósito a prazo**. Através de um pipeline completo (busca, coleta, modelagem, carga e análise), este projeto visa responder perguntas de negócio com base nos dados.

## 🗂️ Estrutura do Projeto

- `data/`: Contém o dataset original ('bank-full.csv','bank_data_tratado.parquet').
- `notebooks/`: Contém notebooks utilizados para análise e ETL.
- `documentacao/`: Documentos de suporte como objetivo, modelagem, catálogo de dados, autoavaliação, etc.

## ⚙️ Pipeline de Engenharia de Dados

1. **Busca e Coleta dos Dados**  
   O dataset foi obtido do UCI Machine Learning Repository.

2. **Modelagem dos Dados**  
   Utilizado modelo em **Esquema Estrela** com uma tabela fato e três dimensões.

3. **Carga e Transformação**  
   Processo ETL feito na plataforma **Databricks Community Edition**, com tratamento, normalização e carga dos dados.

4. **Análise de Qualidade e Negócio**  
   Análise exploratória, validação de atributos, e respostas às perguntas de negócio.

## 📊 Ferramentas Utilizadas

- Databricks Community Edition
- Python (pandas, numpy, sklearn, matplotlib)
- Git e GitHub

## 👨‍💻 Autor

- Nome: Thales Leal
- GitHub: https://github.com/tleal192
