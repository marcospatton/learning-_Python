def loopFor():
    for x in range(5, 10):
        print(x)
loopFor()

#Usandoi um loop for em uma colecao

def loopArray():
    dias = ["seg", "ter", "qua", "qui", "sex","sab", "dom" ]
    for d in dias:
        print(d)
loopArray()


#usando a função enumerate, para buscar valores e seus indices

def loopEnum():
    dias = ["seg", "ter", "qua", "qui", "sex","sab", "dom" ]
    for i, d  in enumerate(dias):
        print(i,d)
loopEnum()