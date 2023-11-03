num1 = float(input("Digite o primeiro valor:"))
num2 = float(input("Digite o segundo valor:"))
op = int(input("Dentre as opções abaixo escolha uma: \n [1] - somar \n [2] - multiplicar \n [3] - maior \n [4] - novos números \n [5] - sair do programa \n escolha:"))

while (op != 5): 
    if op == 1:
        soma = num1 + num2
        print(" A soma entre {} e {} resulta em {}".format(num1,num2,soma))
    elif op == 2:
        multi = num1 * num2
        print(" A multiplicação entre {} e {} resulta em {}".format(num1,num2,multi))
    elif op == 3:
        if num1 > num2:
            print("O maior número é {}".format(num1))
        elif num2 > num1:
            print("O maior número é {}".format(num2))
        else:
            print("Os números são iguais")
    elif op == 4:
        num1 = float(input("Digite o primeiro valor:"))
        num2 = float(input("Digite o segundo valor:"))
        print(" Os novos valores são {} e {}".format(num1,num2))
    else:
        print("Opção inválida")
    num1 = float(input("Digite o primeiro valor:"))
    num2 = float(input("Digite o segundo valor:"))
    op = int(input("Dentre as opções abaixo escolha uma: \n [1] - somar \n [2] - multiplicar \n [3] - maior \n [4] - novos números \n [5] - sair do programa \n escolha:"))
    
print("Programa finalizado!")
