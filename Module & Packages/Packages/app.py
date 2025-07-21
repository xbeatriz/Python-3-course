# import audio.formatos.mp3 as mp3
# from audio.formatos import mp3

# mp3.converter('gatinhos_sorridentes.mp4')  # Chamada da função converter do módulo mp3

####### __name__ == '__main__' ########
# O bloco if __name__ == '__main__': é usado para garantir que o código
# dentro dele só seja executado quando o arquivo for executado diretamente,
# e não quando for importado como um módulo em outro arquivo.
print('app:' + __name__)  # Imprime o nome do módulo atual
if __name__ == '__main__':
# ou seja, se eu criar outro ficheiro e importar o app, e tentar correr o codigo, ele nao vai correr
    import audio.formatos.mp3 as mp3  # Importa o módulo mp3 do pacote audio.formatos
    mp3.converter('gatinhos_sorridentes.mp4')  # Chamada da função converter do módulo mp3
