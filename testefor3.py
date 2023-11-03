print('-=' * 10)
print("TABUADA")
print('-=' * 10)
num = int(input("Escolha um número:"))

for i in range(0,11):
    calculo = num * i 
    print("{} x {} = {}".format(num,i,calculo))
print("fim!")
