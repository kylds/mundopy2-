a1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da p.a: "))


while razao!=0:
    an = a1 + (10 - 1) * razao
    for i in range (a1,an,+razao):
        print("Sequência: {}".format(i))
    a1 = int(input("Digite o primeiro termo: "))
    razao = int(input("Digite a razão da p.a: "))





