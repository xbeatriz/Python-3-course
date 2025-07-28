# sequências especiais

# \d => qualquer digito [0-9]
# \D => qualquer caracteres não dígito [^0-9]
# \s => qualquer caractere espaço em branco [\t\n\r\f\v]
# \S => qualquer caractere não espaço branco [^\t\n\r\f\v]
# \w => qualquer caractere alfanumérico [a-zA-Zà-úÀ-Ú0-9_]
# \W => qualquer caractere não alfanumérico [^a-zA-Zà-úÀ-Ú0-9_]
# \b => começo ou fim da palavra    
# \B => nem no começo nem no fim da palavra

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

regex = r'ta\b' # final da palavra. se fosse inicio da palavra \bta
texto = 'tampa a panela Roberta Batata'
# encontrar(regex, texto, 'findall')
p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m)

print(matches)
# print(next(matches))
# print(next(matches))

print(texto[15:22])
print(texto[22:29])

