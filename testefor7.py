# frase palíndroma 
#colocar tudo pra maiusculo pra facilitar a conversão 
# junto - colocar tudo colado sem espaços 


frase = str(input("Digite uma frase sem colocar os acentos:")).strip().upper()
palavra = frase.split()  # Gerar uma lista com cada palavra separada
junto = ''.join(palavra)
inv = ''


#também pode ser inv = junto[::-1] para substituir o for 

# Inverter a frase
for letra in range(len(junto) - 1, -1, -1):
    inv += junto[letra]

# Verificar se é um palíndromo
if junto == inv:
    print("Essa frase é palíndroma")
else:
    print("Essa frase não é palíndroma")

