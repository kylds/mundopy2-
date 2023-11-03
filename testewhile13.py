cont = 0 
m = 0 
cont_20 = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo [M/F]: ")).upper()
    if sexo!= 'M' and sexo!='F':
        print("Inválido")
    if idade > 18:
        cont +=1
    if sexo == 'M':
        m +=1 
    if sexo == 'F' and idade < 20:
        cont_20 += 1 
    p = str(input("Deseja continuar o programa? [sim/não]")).upper()
    if p == 'NÃO':
        break 
print("Quantidade de pessoas com mais de 18 anos: {}".format(cont))
print("Quantidade de homens cadastrados: {}".format(m))
print("Quantidade de mulheres menores que 20 anos: {}".format(cont_20))
