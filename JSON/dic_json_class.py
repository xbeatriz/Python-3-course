# JSON
# JavaScript Object Notation
# JSON / PYTHON
# object - dict
# array - list
# string - str
# number(int) - int
# number(float) - float
# true - True
# false - False
# null - None

string_cadastro = '''
{
    "dados": [
        {
            "usuario": "ana",
            "idade": 20,
            "altura": 1.59,
            "email": null,
            "ativado": false
        },
        {
            "usuario": "pedro",
            "idade": 26,
            "altura": 1.81,
            "email": "pedrinho@email.com",
            "ativado": true
        }
    ]
}
'''
# JSON para dicionário
import json

dados = json.loads(string_cadastro)
print(dados)
type(dados['dados'])

for dado in dados['dados']:
    print('altura',dado['altura'])
    print('idade',dado['idade'])

for dado in dados['dados']:
    del dado['idade']

print(dados)

# dicionário para JSON
json_string = json.dumps(dados)
print(json_string)
json_string = json.dumps(dados, indent=2)
print(json_string)
json_string = json.dumps(dados, indent=2, sort_keys=True)
print(json_string)

# dicionário para arquivo JSON
type(dados)
print(dados)

with open('json/novo_json.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json, indent=2)

# Ler arquivos JSON
with open('json/novo_json.json') as arquivo_json:
    novo_dicionario = json.load(arquivo_json)

for dado in novo_dicionario['dados']:
    print(dado['email'])