# expressões regulares
# são padrões 

import re # regular expression ou regex 

padrao = re.compile('abc')
print(padrao)

# encontra o padrao ( adicionado em cima) dentro do texto que nós colocamos
m = padrao.match('abcd') # em vez de match também posso usar .search MAS 
print(m.group())

# o search procura ao longo de toda a string, enquanto que o match so procura no inicio
s  = padrao.search('bcd abc') # se eu fizer isto mas com match, ele dará erro
print(s.group())

# o findall, diz-nos todas as aparições do nosso padrao ao longo da string
f = padrao.findall('bcd abc abc')
print(f)

def encontrar(regex, texto, opcao = 'match'):
    """opcao ==> match, search ou findall"""
    p = re.compile(regex)
    m = p.__getattribute__(opcao)(texto)
    if m: 
        if opcao != 'findall':
            return print(m.group())
        return print(m)
    
regex = 'abc'
texto = 'bcd abc'
print(encontrar(regex, texto))
encontrar(regex, texto, 'search')
encontrar(regex, texto, 'findall')