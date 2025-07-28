# sequências especiais

# \d => qualquer digito [0-9]
# \D => qualquer caracteres não dígito [^0-9]
# \s => qualquer caractere espaço em branco [\t\n\r\f\v]
# \S => qualquer caractere não espaço branco [^\t\n\r\f\v]
# \w => qualquer caractere alfanumérico [a-zA-Zà-úÀ-Ú0-9_]
# \W => qualquer caractere não alfanumérico [^a-zA-Zà-úÀ-Ú0-9_]

import re 

def encontrar(regex, texto, opcao = 'match'):
    """opcao ==> match, search ou findall"""
    p = re.compile(regex)
    m = p.__getattribute__(opcao)(texto)
    if m: 
        if opcao != 'findall':
            return print(m.group())
        return print(m)
    
regex = '[\d$]+'
texto = 'O preço é [200$] palavra_junta'
encontrar(regex, texto, 'findall')

regex = '[\w]+'
texto = 'O preço é [200$] palavra_junta'
encontrar(regex, texto, 'findall')