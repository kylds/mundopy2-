cont = 0 
i = 0

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    i += 1
    cont += n 
    # a variavel tem que ficar nesse lugar 
    # se ficar antes do if vai contar o 999 pois é um n digitado
print("Soma dos {} números foi {}".format(i,cont))