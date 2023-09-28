# Dado um nome "Alexandra Oliveira" escrevê-lo normalizado  "Oliveira, Alexandra"

nome = "Gabriela Carneiro Macieira"
lista = nome.split()
resultado = lista[-1] + ","
outros = lista [:-1]
for n in outros:
    resultado = resultado +" " + n 
    print(resultado)
