raise ValueError('Valor inválido')


try:
    raise NameError('Nome')
except NameError:
    print('Ocorreu um erro de nome')
    raise
