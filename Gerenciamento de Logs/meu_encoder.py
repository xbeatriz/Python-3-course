from app import log_manager

logger = log_manager(name='meu_encoder',
filename='meu_encoder.log',
log_level='DEBUG',handler_level='ERROR')

def logs(func):
    def log_encoder(*args, **kwargs):
        try:
            resultado = func(*args, **kwargs)
        except UnicodeEncodeError:
            logger.exception('*********************UnicodeEncodeError***************************')
        else:
            logger.debug(f'Rodou "{func.__name__}" com {args}, {kwargs} => {resultado}')
            return resultado
    return log_encoder

s = 'mãe'

@logs
def meu_encoder(s, *args, **kwargs):
    return s.encode(*args, **kwargs)

meu_encoder(s, encoding='cp437')
meu_encoder(s, encoding='cp437', errors='ignore')
meu_encoder(s, encoding='cp437', errors='xmlcharrefreplace')
meu_encoder(s, encoding='utf8')
