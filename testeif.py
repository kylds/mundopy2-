casa = float(input("Qual o valor da casa:"))
sal = float(input("Qual o seu salário:"))
anos = int(input("Em quantos anos pretende pagar a casa:"))

minimo = sal * 30/100

parcelas = (casa / (anos * 12)) #multiplicado por 12 que é a quantidade de meses do ano 
if parcelas >= minimo:
    print("Infelizmente você não pode financiar essa casa")
    print("Valor das parcelas {:.4f}".format(parcelas))
else:
    print("Você pode financiar essa casa")
    print("Valor das parcelas {:.4f}".format(parcelas))