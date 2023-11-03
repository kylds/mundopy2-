valor = float(input("Digite o valor do produto:"))
pag = int(input("Forma de pagamento: \n 1 - Á vista dinheiro/cheque \n 2 - Á vista no cartão \n 3 - 2X no cartão \n 4 - 3X ou mais no cartão \n Digite a opção:"))
if pag == 1:
    percentual = 10/100
    desconto = valor * percentual
    novo_valor = valor - desconto 
    print("O valor a ser pago é R$ {}".format(novo_valor))
elif pag == 0 or pag >4:
    print("Digito inválido! Reinicie o programa")
    print("Sua compra de {} vai custar {} no final".format(valor,valor))
elif pag == 2:
    percentual = 5/100
    desconto = valor * percentual
    novo_valor = valor - desconto 
    print("O valor a ser pago é R$ {}".format(novo_valor))
elif pag == 3:
    div = (valor/ 2)
    print("Compra parcelada em 2X no cartão de {}".format(div))
    print("Sua compra de {} vai custar {} no final".format(valor,valor))
else:
    if pag == 4:
        parcelas = int(input("Quantidade de parcelas:"))
        percentual = 20/100
        total = valor + (valor * percentual)
        novo = total / parcelas
        print("Sua compra de {}x ou mais no cartão será de {:.2f} COM JUROS".format(parcelas,novo))
        print("Sua compra de {} vai custar {:.2f} no final".format(valor,total))
    else:
        print("Reinicie o programa!")