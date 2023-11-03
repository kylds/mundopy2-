a1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da p.a: "))
t = 10
cont = 0

while razao!=0:
    an = a1 + (t - 1) * razao
    for i in range (a1,an,+razao):
        print("Sequência: {}".format(i))
    termos = int(input("Você quer mais termos? digite a quantidade:"))
    if termos > 0:
        tot = termos + t 
        an = a1 + (tot - 1) * razao
        for c in range (a1,an,+razao):
            print("Sequência: {}".format(c))
    a1 = int(input("Digite o primeiro termo: "))
    razao = int(input("Digite a razão da p.a: "))
    cont += 1
    if termos == 0:
        print("Programa finalizado")
        print("Quantidade de p.a: {}".format(cont))
        
    
