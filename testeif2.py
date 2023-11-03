# rever!!!!!!!!!
num = int(input("Digite um número inteiro:"))
base = int(input("Escolha a base de conversão: \n 1 - binário \n 2 - octal \n 3 - hexadecimal \n"))
dividendo = num 
lista = []
lista_2 = []
lista_3 = []

# para passar de decimal para binário e octal 
# o dividendo tem que ser dividido inteiramente e depois pega o resto enquanto o resultado for maior que 0 

if base == 1:
    while dividendo > 0:
        lista.insert(0, dividendo % 2)
        dividendo = dividendo // 2
    print("Seu número em binário é {}".format(lista))
elif base == 2:
    while dividendo > 0:
        lista_2.insert(0, dividendo % 8)
        dividendo = dividendo // 8
        print("Seu número em octal é {}".format(lista_2))
else:
    print()



