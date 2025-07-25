# replicando dicionário
# tratando chaves não encontradas

d = dict([('1', 'um'), ('4', 'quatro')])
print(d)
# print(d['2']) - dá erro
print(d['4'])

print(d.get('4'))
# d.get(1) - não acontece nada
print(d.get(1, 'não encontrado!'))

print(d.get('4', 'não encontrado'))

class StrDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try: 
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

dicionario = StrDict({'2': 'dois', '4': 'quatro'})
print(dicionario)

# ele encontra os dois tipos, quer str quer int, proque este é transformado em string
print(dicionario[4])
print(dicionario['4'])
