import re 

def encontrar(regex, texto, opcao = 'match'):
    """opcao ==> match, search ou findall"""
    p = re.compile(regex)
    m = p.__getattribute__(opcao)(texto)
    if m: 
        if opcao != 'findall':
            return print(m.group())
        return print(m)

regex = r'([a-zA-Z0-9-_]+)@([a-zA-Z0-9-_]+)\.(\W+)'
texto = """
Tetxo antes
ga_to@gmail.com
pa-to@ahoo.com
No meio alguns textos
pata1995@meu-email.edu
rato2020@hotmail.com
k@email.net
E depois alguns textos
"""
# encontrar(regex, texto, 'findall')

p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m.group())

regex = r'https?://(www\.)?(\w+)\.(com|net|org)(\.\w+)?'
texto = """"
Sites
https://www.meusite.com
http://outrosite.net
https://google.com
https://www.site.org
http://siteprotugues.com.pt
"""
p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m.group())