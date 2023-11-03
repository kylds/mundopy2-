
soma = 0
cont = 0
for i in range (1,501,2):
    if i%3 ==0:
        cont += 1
        soma = soma + i 
print("A Soma dos {} números dá {}".format(cont,soma))    

# soma += 1 vai estar contando a quantidade números que são múltiplos de 3
# precisar ser soma = somar + i para que o programa some os números a cada i vezes que ele obedecer a regra 
