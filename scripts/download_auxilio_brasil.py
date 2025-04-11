import requests

url = 'https://raw.githubusercontent.com/tleal92/engenharia-dados-clima-rj/main/datasets/202301_AuxilioBrasil.csv'
output_path = '../data/auxilio_brasil.csv'

response = requests.get(url)
with open(output_path, 'wb') as f:
    f.write(response.content)

print("Download concluído com sucesso!")
