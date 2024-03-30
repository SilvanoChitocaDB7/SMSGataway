#Biblioteca usada para criação e manipulação de JSON
import json
#Biblioteca usada para fazer requisições HTTP (deve ser instalada)
import requests

#Api endpoint (o link que será usado para enviar as mensagens)
url = "https://api.useombala.ao/v1/messages"

#Mensagem
# Data - Conteúdo da mensagem
# from - Remetente(o teu número)
# to - Destinatário (o número do destinatário da mensagem)
data = {
"message": "Mensagem de teste.",
"from": "9XXXXXXXX",
"to": "9XXXXXXXX",
}

#Cabeçalho da mensagem com as específicações do SMSGateway provider (Authorization, Content-Type)
headers = {"Authorization" : "Token 357r185f-ac81-4da1-a03f-85e85d5c8657","Content-Type":"application/json"}

#Envio da requisição (Endpoint, header, Dados da mensagem no formato JSON)
response = requests.post(url, headers=headers, json=json.dumps(data))

# Codigo da resposta do servidor (201 para sucessso)
print(response.status_code)
