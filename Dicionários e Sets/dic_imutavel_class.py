# dicionário imutável 
from types import MappingProxyType

d = {'1': 'um', '2': 'dois'}

d_prx = MappingProxyType(d)
print(d_prx)
print(d_prx['2'])
print(d_prx.get('1'))

