nome = "Daniella Monteiro Cavalheiro"

def normaliza(nome):
    lista = nome.split()
    resultado = lista[-1] + ","
    outros = lista [:-1]
    for n in outros:
        resultado = resultado +" " + n 
    print(resultado)

normaliza(nome)
normaliza("Daniella Cavalheiro")
nome = input("Qual o teu nome?")
print (normaliza(nome))
