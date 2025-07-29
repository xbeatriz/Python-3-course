# Back End     << API >>     Front End

import requests

URL = 'https://reqres.in'
endpoint = '/api/users/2'
requisicao = URL + endpoint
print(requisicao)

usuario = requests.request('GET', requisicao)
print(usuario)

resposta = usuario.json()
print(resposta)

resposta['data']['avatar']

