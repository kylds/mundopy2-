from time import sleep 
import random 

print('-' * 20)
print("JOGO DA ADVINHAÇÃO")
print('-' * 20)
cont = 0

num = int(input(("Em que número você acha que estou pensando: ")))
numero = random.randint(0,11)
#toda vez que usar randint precisa colocar dessa forma!!

print('...')
sleep(2)

while (num!=numero):
    cont += 1
    print("Você errou! tente novamente")
    num = int(input(("Em que número você acha que estou pensando: ")))
    numero = random.randint(0,11)
print('...')
sleep(3)
print("Número de palpites até acertar: {}".format(cont))
