
for i in range(1,5):
        num = int(input("Digite um número:"))
        if num == 0 or num == 1:
             print("Programa finalizado! um número só pode ser primo se for maior que 1 e também não pode ser 1, Digite outro número!")
        elif num % num == 0 and num % 1 == 0:
            if num == 2 or num == 5 or num == 7:
                 print("O número {} é um número primo!".format(num))
            elif num % 2 == 0:
                 print("O número {} não é um número primo!".format(num))
            elif num % 5 == 0:
                 print("O número {} não é um número primo!".format(num))
            elif num % 7 == 0:
                 print("O número {} não é um número primo!".format(num))
            else:
                 print("O número {} é um número primo!".format(num))
        else:
            print("O número {} não é um número primo!".format(num))