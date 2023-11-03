#fatorial 
import math 

#para calcular o fatorial direito ele tem que estar dentro do loop
#para que ele possa atualizar o fatorial a cada numero diferente de 0

print("Para finalizar o programa digite -1")
num = int(input("Digite um número: "))

while num!=-1:
    numero = math.factorial(num)
    print("Fatorial de {}! = {}".format(num,numero))
    num = int(input("Digite um número: "))
    #o num precisa vim por último pra quando pegar o primero num e fizer o fatorial ele poder ser atualizado e continuar até ser o contrário de -1

print("Programa finalizado")