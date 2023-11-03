print('-' * 20)
print("TABUADA")
print('-' * 20)

while True:
    n = int(input("Digite o número que deseja ver a tabuada: "))
    if n == -1: #colocar antes para finalizar o programa e não pegar a tabuada do -1
        break
    for i in range(0,11):
        multi = n * i
        print(" {} x {} = {}".format(n,i,multi)) 
    