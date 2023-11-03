from math import pow 
peso = float(input("Informe o peso:"))
altura= float(input("Informe a altura:"))

imc = peso / pow(altura,2)

if imc <= 18.5:
    print("Seu IMC: {:.2f}".format(imc))
    print("Abaixo do peso")
elif imc > 18.5 and imc <= 25:
    print("Seu IMC: {:.2f}".format(imc))
    print("Peso ideal")
elif imc > 25 and imc <= 30:
    print("Seu IMC: {:.2f}".format(imc))
    print("Sobrepeso")
elif imc > 30 and imc <= 40:
    print("Seu IMC: {:.2f}".format(imc))
    print("Obesidade")
else:
    print("Seu IMC: {:.2f}".format(imc))
    print("Obesidade mórbida")