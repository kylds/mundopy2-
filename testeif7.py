num_1 = float(input("Digite um valor:"))
num_2 = float(input("Digite um valor:"))
num_3 = float(input("Digite um valor:"))

if num_1 + num_2 > num_3 and num_2 + num_3 > num_1 and num_3 + num_1 > num_2:
    print("Esse triângulo pode ser formado!")
    if num_1 == num_2 == num_3:
        print("Esse triângulo é equilátero")
    elif num_1 == num_2 or num_2 == num_3 or num_3 == num_1:
        print("Esse triângulo é isosceles")
    else:
        print("Esse triângulo é escaleno")
else:
    print("Esses valores não formam um triângulo!")