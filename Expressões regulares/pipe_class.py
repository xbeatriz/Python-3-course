# | => A|B ou B uma coisa ou outra
import re 

def encontrar(regex, texto, opcao = 'match'):
    """opcao ==> match, search ou findall"""
    p = re.compile(regex)
    m = p.__getattribute__(opcao)(texto)
    if m: 
        if opcao != 'findall':
            return print(m.group())
        return print(m)
    

regex = r'Ta\B|ta\B' # final da palavra. se fosse inicio da palavra \bta
texto = 'Tampa a panela Roberta Batata'
# encontrar(regex, texto, 'findall')
p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m)

regex = r'eu@(gmail|hotmail).com'
texto = 'eu@gmail.com e eu@hotmail.com'
# encontrar(regex, texto, 'findall')
p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m.group(0))
    print(m.group(1))
