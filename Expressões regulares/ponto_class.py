# . ponto => faz o match com qualquer caracter

import re 

def encontrar(regex, texto, opcao = 'match'):
    """opcao ==> match, search ou findall"""
    p = re.compile(regex)
    m = p.__getattribute__(opcao)(texto)
    if m: 
        if opcao != 'findall':
            return print(m.group())
        return print(m)
    
regex = r'.' # todos os caracteres
texto = 'O preço é de [$200]. Palavra_junta'
print(encontrar(regex, texto, 'findall'))

regex = r'.' # todos os caracteres
texto = 'exemplo do site.com ou o email eu@gmail.com'
print(encontrar(regex, texto, 'findall'))

regex = r'\.'  # encontrar apenas o ponto
texto = 'exemplo do site.com ou o email eu@gmail.com'
print(encontrar(regex, texto, 'findall'))

regex = r'\w@?\w+\.com'  # encontrar apenas o ponto
texto = 'exemplo do site.com ou o email eu@gmail.com'
print(encontrar(regex, texto, 'findall'))