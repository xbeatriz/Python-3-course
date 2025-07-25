from collections import namedtuple

Vestido = namedtuple('Vestido', ['nome', 'tamanho', 'cor', 'quantidade'])
vestido = Vestido('vestido', 'm', 'azul', 20)


itens = vestido._asdict().items()

print(itens)

meu_dicionario = {chave.capitalize(): valor for chave, valor in itens}
print(meu_dicionario)


