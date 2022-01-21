# Declarando e inicializando uma variárvel

f =0
print(f)


#declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variável de tipos diferente

print("Isto é uma string " + str(123))

#variável global x variável local

def Algumafuncao():
    global f
    f = "def"
    print(f)

    Algumafuncao()
    print(f)