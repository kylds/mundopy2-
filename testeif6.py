ano = int(input("Digite o ano de nascimento:"))

if ano >= 2014:
    print("Natação mirim")
elif ano >= 2009 and ano < 2014:
    print("Natação infantil")
elif ano >= 2004 and ano < 2009:
    print("Natação junior")
elif ano >= 2003 and ano < 2004:
    print("Natação senior")
else:
    ano > 2003 
    print("Natação master")