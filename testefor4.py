print('-=' * 10)
print("Somatório!")
print('-=' * 10)

for i in range(0,7):
    num = int(input("Digite um número:"))
    if num%2 == 0:
        num = num + i  
print("Soma = {}".format(num))

