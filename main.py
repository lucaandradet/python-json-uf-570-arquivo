import json
import urllib.request

#Carrega um JSON
url = 'https://sisu-api-pcr.apps.mec.gov.br/api/v1/oferta/instituicao/570'
with urllib.request.urlopen(url) as response:
  resp = response.read()

#Faz a análise desse JSON.
resp = json.loads(resp.decode('utf-8'))

#Itera por todos os itens do dicionário principal....
with open('dados.json', 'w') as json_file:
  for k, dados in resp.items():
    if dados != 'UFRN - UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE':
      #print(dados)                  #imprime o valor de dados
      json.dump(dados, json_file, indent=2)
    else:
      valor = "Não salva"