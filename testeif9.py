#jokenpo 
# printar o jogo do pc - print("Computador jogou {}".format(itens[computador]))
# mesma coisa pra printar o do jogador! 

import random  
from time import sleep
print("Vamos jogar!")
jogador = int(input("1 - pedra \n 2 - papel \n 3 - tesoura \n Informe o digito:"))
jogo = random.randint(1,3)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(1)
if jogador > 3:
    print("Número inválido! Reinicie o jogo")
elif jogador == jogo:
    print("Números iguais! Reinicie o jogo")
elif jogador == 1:
    if jogo == 2:
        print("Você venceu!")
        print("Papel  ganha da pedra")
    else:
        print(" perdeu!")
        print("Tesoura perde para pedra")
elif jogador == 2:
    if jogo == 1:
        print("Você perdeu!")
        print("Papel ganha da pedra")
    else:
        print("Você ganhou!")
        print("Papel perde para a tesoura")
else:
    if jogo == 1:
        print("Você perdeu!")
        print("Pedra ganha da tesoura")
    else:
        print("Você ganhou!")
        print("Pedra perde para o papel")