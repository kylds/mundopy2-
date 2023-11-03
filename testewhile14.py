print('-='* 30)
print("CARRINHO DE COMPRAS")
print('-='* 30)

gasto = 0
maior_1000 = 0
lista_p = []
lista_n = []
c = 0 #guarda o índice do for 

while True: 
    preco = float(input("Digite o preço do produto: "))
    nome = str(input("Digite o nome do produto: ")) 
    lista_p.append(preco)
    lista_n.append(nome)
    gasto += preco
    if preco >= 1000:
        maior_1000 += 1
    cont = str(input("Deseja continuar? [S/N]: ")).upper()
    if cont == 'N':
        break 


valor_barato_p = 9999 #variavel de compração
nome_p = ''

for i in range(len(lista_p)):
    if lista_p[i] < valor_barato_p:
        valor_barato_p = lista_p[i] #a variavel vai guardar o índice do menor valor da lista
        nome_p = lista_n[i]
        c = i 

        
print("Total do carrinho: {} ".format(gasto))
print("Produtos que custam mais de R$1000: {}".format(maior_1000))
print("Produto mais barrato é {} e custa R${}".format(lista_n[c],lista_p[c]))
    

