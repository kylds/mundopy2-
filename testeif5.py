nota_1 = float(input("Digite a primeira nota:"))
nota_2 = float(input("Digite a segunda nota:"))
media = (nota_1 + nota_2) / 2

if media <= 5:
    print("A média do aluno é {:.1f}".format(media))
    print("Reprovado!")
elif media > 5 and media <= 6.9:
    print("A média do aluno é {:.1f}".format(media))
    print("Recuperação!")
else:
    print("A média do aluno é {:.1f}".format(media))
    print("Aprovado!")