# copiar imagens

with open('Leitura e Escrita de arquivos/image.png', 'rb') as minha_imagem: # rb ==> read bytes
    with open('Leitura e Escrita de arquivos/image_copy.png', 'wb') as minha_imagem_copia: # wb ==> write bytes
        for byte in minha_imagem: 
            minha_imagem_copia.write(byte)

with open('Leitura e Escrita de arquivos/image.png', 'rb') as minha_imagem:  # rb => read bytes
    with open('Leitura e Escrita de arquivos/image_copy2.png', 'wb') as minha_imagem_copia2:  # wb => write bytes
        bloco_de_bytes = 4000
        imagem_bloco = minha_imagem.read(bloco_de_bytes)
        while len(imagem_bloco) > 0:
            minha_imagem_copia2.write(imagem_bloco)  
            imagem_bloco = minha_imagem.read(bloco_de_bytes)
