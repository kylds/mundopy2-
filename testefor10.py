lista_id_H = []
list_id_M = []
lista_n_H = []
list_n_M = []
total = 0
menor_q_vinte = 0

for i in range(4):
    nome = str(input("Digite seu nome:"))
    idade = int(input("Digite sua idade:"))
    sexo = str(input("Digite seu sexo (F ou M):"))
    if (sexo == "M"):
         lista_n_H.append(nome)
         lista_id_H.append(idade)
    elif (sexo == "F"):
         list_n_M.append(nome)   
         list_id_M.append(idade)
         if (idade > 20):
                menor_q_vinte+= 1
    total += idade
          
mais_velho_nome = ''
mais_velho_idade = 0
for i in range(len(lista_id_H) - 1):
      if (lista_id_H[i] > mais_velho_idade):
            mais_velho_idade = lista_id_H[i]
            mais_velho_nome = lista_n_H[i]

print("O homem mais velho do grupo tem {} anos e se chama {}".format(mais_velho_idade,mais_velho_nome))
print("A quantidade de mulheres menores que 20 anos é de {}".format(menor_q_vinte))
print("A média das idades é {}".format(total/4))
