#caixa eletrônico 
#cedulas de 50,20,10 e de 1 

lista = []
c = 0 
v = 0
d = 0
u = 0 


print('-=' * 10)
print("BANCO")
print('-=' * 10)



while True:
    valor = int(input("Digite o valor sacado: R$ "))
    lista.append(valor)
    for i in range(len(lista)):
        if lista[i] >= 50:
            c = lista[i] // 50
            rc = lista[i] % 50 
            if lista[i] % 50 != 0:
                   v = rc // 20
                   rv = lista[i] % 20 
                   if lista[i] % 20 != 0:
                          d = rv // 10
                          rd = lista[i] % 10
                          if lista[i] % 10 != 0:
                                 u = rd // 1  
                                 
    p = str(input("Desejar digitar outro valor? [S/N]: ")).upper()
    if p == 'N':
        break

print('-' * 20)
print("{} notas de 50 reais".format(c))
print("{} notas de 20 reais".format(v))
print("{} notas de 10 reais".format(d))
print("{} notas de 1 real".format(u))
print('-' * 20)
 