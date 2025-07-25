# variação de dicionários

import collections

# OrderedDict
d = {'1': 'um', '2': 'dois'}
od = collections.OrderedDict(d)
print(od)

# Conter
c = collections.Counter('araraquara')
print(c)
print(c.most_common())
print(c.most_common(2))

# ChainMap
e = {'3': 'tres', '4': 'qautro'}
print(e)

cm = collections.ChainMap(d, e)
print(cm)
print(cm['1'])
print(cm.get('2'))
