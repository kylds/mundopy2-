lista = []

for i in range (5):
    peso = float(input("Digite o peso:"))
    lista.append(peso)
print("O menor peso é {}".format(min(lista)))
print("O maior peso é {}".format(max(lista)))