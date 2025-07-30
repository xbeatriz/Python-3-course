from app import log_manager

logger = log_manager(name='op_matematicas',
filename='op_matematicas.log',
log_level='DEBUG',handler_level='ERROR')


def soma(*args):
    s = sum(args)
    logger.debug(f'Soma {args} = {s}')
    return s

def media(*args):
    m = sum(args)/len(args)
    logger.debug(f'Média {args} = {m}')
    return m

def divisao(*args):
    """ Múltiplos números em (a,b) de forma tal que a/b """
    resultados = []
    for ab in args:
        for a,b in ab:
            try:
                resultados.append(a/b)
            except ZeroDivisionError:
                logger.exception('Tentou dividir por zero!')
    logger.debug(f'Divisões {args} = {resultados}')
    return resultados

soma(2,3,4,6)

media(4,2,5,43,12)

divisao([(12,3), (8,0), (3,1)])
