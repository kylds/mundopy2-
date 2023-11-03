num = int(input("Digite um número:"))
cont = 0

while num != 999:
    cont += num 
    num = int(input("Digite um número:"))
print("Soma dos números digitados: {}".format(cont))