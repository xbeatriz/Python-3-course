
def log_manager(name='exemplo',
              log_level='DEBUG',
              log_format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
              filename='exemplo.log',
              handler_level='DEBUG'):

    import logging          

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging,log_level)) # logging.DEBUG

    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(getattr(logging,handler_level))
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


if __name__ == '__main__':
    import arquivo_logs_class
    import meu_encoder
    import op_matematica_class