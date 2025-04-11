# Catálogo de Dados

## Fonte

- Dataset: Bank Marketing
- Origem: UCI Machine Learning Repository

## Tabela Fato

### Fato_Adesao
- age (int): Idade do cliente
- job (str): Tipo de trabalho
- marital (str): Estado civil
- education (str): Escolaridade
- default (str): Se tem inadimplência
- housing (str): Possui financiamento habitacional
- loan (str): Possui empréstimo pessoal
- contact (str): Tipo de contato
- month (str): Mês da última campanha
- day_of_week (str): Dia da semana da última campanha
- duration (int): Duração da chamada (em segundos)
- campaign (int): Número de contatos durante esta campanha
- pdays (int): Dias desde o último contato
- previous (int): Número de contatos anteriores
- poutcome (str): Resultado da campanha anterior
- emp.var.rate (float): Taxa de variação de emprego
- cons.price.idx (float): Índice de preços ao consumidor
- cons.conf.idx (float): Índice de confiança do consumidor
- euribor3m (float): Taxa de juros
- nr.employed (float): Número de empregados
- y (str): Cliente aderiu ao produto? ('yes' ou 'no')

## Domínios de Atributos

- age: 18 a 95
- job: admin., technician, services, management, etc.
- education: basic.4y, high.school, university.degree, etc.
- y: yes, no