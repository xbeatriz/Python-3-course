print('mp3:' + __name__)  # Imprime o nome do módulo atual

def converter(arquivo):
    """
    Função que converte um arquivo de áudio para o formato MP3.
    meuvideo.mp4 ==> meuvideo.mp3
    """
    "meuvideo.mp4".split('.')  # Divide o nome do arquivo em partes usando o ponto como separador
    ['meuvideo', 'mp4'][0] # Resultado da divisão do nome do arquivo
    print(arquivo.split('.')[0] + '.mp3')  # Imprime o nome do arquivo a ser convertido

 