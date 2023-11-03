from random import randint

print('=' * 20)
print("PAR OU ÍMPAR")
print('=' * 20)

cont = 0

while True:
    jogo = int(input("Digite um valor: "))
    escolha = str(input("Ímpar ou par? [P/I]: "))
    pc = randint(0,999)
    s = pc + jogo 
    if escolha != 'P' and escolha != 'I':
        print("Valor inválido")
    if escolha == 'P':
        print(" O computador jogou {} e você jogou {}".format(pc,jogo))
        print("Total = {}".format(s))
        if s % 2 == 0:
            print('Você ganhou!')
            cont +=1 
        else:
            print("Você perdeu!")
            print('Você venceu {} vezes'.format(cont))
            break 
    if escolha == 'I':
        print(" O computador jogou {} e você jogou {}".format(pc,jogo))
        print("Total = {}".format(s))
        if s % 2 != 0:
            print('Você ganhou!')
            cont +=1 
        else:
            print("Você perdeu!")
            print('Você venceu {} vezes'.format(cont))
            break 
    