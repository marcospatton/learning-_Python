def EscreveArquivo():
    arquivo = open("NovoArquivo.txt", "w+")

    arquivo.write("Linha gerada com a função 'EscreveArquivo' \r\n")

    arquivo.close()

#EscreveArquivo()

def AlteraArquivo():
    arquivo = open("NovoArquivo.txt", "a+")

    arquivo.write("Linha gerada com a função 'AlteraArquivo' \r\n")

    arquivo.close()

AlteraArquivo()