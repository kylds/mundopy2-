#sequência de fibonacci 

# a sequência é a soma dos anteriores para resultar o sucessor 
# os dois primeiros termos são repetidamente 1 

n = int(input("Para interromper o programa digite - 1 \n Digite o número de termos: "))

while n!= -1:
    a0 = 0 
    a1 = 1 
    lista = [a1]
    for i in range(n):
        lista.append(a1)
        a0 = a1
        a1 = a0 + a1
    print("Sequência: {}".format(lista))
    n = int(input("Para interromper o programa digite - 1 \n Digite o número de termos: "))



