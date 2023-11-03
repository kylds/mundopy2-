total = 0
tot = 0
for i in range (7):
    data = int(input("Digite a data de nascimento:"))
    if data <= 2005:
        total += 1 # se fizer total += i, vai ta somando com a variável e vai dar o resultado errado 
    else:
        tot += 1
print("Total de pessoas acima dos 18 anos = {}".format(total))
print("Total de pessoas abaixo dos 18 anos = {}".format(tot))
# vai fazendo += 1 por que a cada input em que adentrar dentro do if ou do else vai add uma pessoa 
# dando o resultado total 