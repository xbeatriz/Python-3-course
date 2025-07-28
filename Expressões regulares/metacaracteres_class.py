# metacaracteres
# ' . ^ $ * + ? { } [ ] \ | ( )

print(' . ^ $ * + ? { } [ ] \ | ( )')

import re 

def encontrar(regex, texto, opcao = 'match'):
    """opcao ==> match, search ou findall"""
    p = re.compile(regex)
    m = p.__getattribute__(opcao)(texto)
    if m: 
        if opcao != 'findall':
            return print(m.group())
        return print(m)
    
regex = '[abc]+' # ele vai tentar um match do abc, assim que ele encontra um caracter pára. MAS se adicionarmos o '+' ele considera um ou mais caracteres que estejam dentro dos []
texto = 'abcd abc'
print(encontrar(regex, texto))

# caracteres do a até ao c (se tiver sem o + ele pega apenas a primeira letra)
regex = '[a-c]+'
texto = 'abcd abc a-c significa caracteres do a até o c'
encontrar(regex, texto, 'findall')

# vai dar me a resposta das palavras completas
regex = '[a-z]+'
texto = 'abcd abc a-c significa caracteres do a até o c' # se tiver palavras maiusculas, ele nao vai encontrar essas mesmas 
encontrar(regex, texto, 'findall')

# responde com as maisculas também
regex = '[a-zA-Z]+' # desta forma já encontra as letras maiusculas, mas nao pega ainda os acentos
texto = 'abcd abc a-c Significa Caracteres do a até o c' 
encontrar(regex, texto, 'findall')

# aparecem com os acentos agora só minusculas
regex = '[a-zA-Zà-ú]+' # desta forma já encontra as letras maiusculas, mas nao pega ainda os acentos
texto = 'É preciso adicionar à-ú para detetar acentuação\
    para letras minúsculas' 
encontrar(regex, texto, 'findall')

# aparecem com os acentos agora em minusculas e maisculas
regex = '[a-zA-Zà-úÀ-Ú]+' 
texto = 'É preciso adicionar à-ú para detetar acentuação'
encontrar(regex, texto, 'findall')

# para encontrar números
regex = '[a-zA-Zà-úÀ-Ú0-9]+' 
texto = '0-9 para detectar números como 13, 18, 243, 7.'
encontrar(regex, texto, 'findall')

# E se eu quiser tudo EXCETO algo? ^
regex = '[^0-9]+' # encontrar tudo EXCETO os números
texto = '0-9 para detectar números como 13, 18, 243, 7.'
encontrar(regex, texto, 'findall')

regex = '[0-9$]+'
texto = 'O preço é de 71$.'
encontrar(regex, texto, 'findall')

regex = '[a-zA-Z_]+' # underline
texto = 'O preço é de 71$ palavras_junta.'
encontrar(regex, texto, 'findall')

regex = '[a-zA-Z0-9$_\[\]]+' # parenteses retos
texto = 'O preço é de [71$] palavras_junta.'
encontrar(regex, texto, 'findall')




