num = int(input("Digite um número: "))
print("Digite -1 se quiser para o programa")
cont = 0 
soma = 0 
lista = []

while (num!= -1):
    soma += num 
    cont += 1 
    media = (soma/cont)
    lista.append(num)
    num = int(input("Digite um número: "))
    print("Digite -1 se quiser para o programa")
    
print("A média dos números é {:.2f}".format(media))
print(" Maior número: {}".format(max(lista)))
print(" Menor número: {}".format(min(lista)))
