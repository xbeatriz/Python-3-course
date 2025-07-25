# UserDict 
# Implementação pura do Python para mapeamentos que funciona como um dicionário padrão. Diferente de OrderedDict, ChainMap e Counter que já vêm
# prontos para uso, o UserDict foi feito para ser usado como subclasse. 
# O UserDict não herda dict, mas possui uma instância interna dict, chamada data, que possui os itens. O que evita recursões ao implementar
# métodos especiais como __setitem__ e simplifca o código de __contains__ 

import collections

class StrDictUser(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item

d = {'1': 'um', '2': 'dois'}
d = StrDictUser(d)
print(d)
print(d['1'])
print(d[1])
d[3] = 'tres'
print(d)