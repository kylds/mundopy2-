ano = int(input("Digite seu ano de nascimento:"))

if (ano>=2005):
    if ano == 2005:
        print("Seu alistamento é esse ano!")
    else:
        t = ano - 2005
        print("Ainda vai se alistar no período militar")
        print("Seu alistamento é em {} anos".format(t))
elif ano>= 1970:
    alis = ano + 18
    print("Seu alistamento ainda é possível!")
    print("Você deveria ter se alistado em {}".format(alis))
else:
    print("Passou do tempo de alistamento")
    tempo = 2005 - ano
    print("Já passou {} anos do seu alistamento".format(tempo))