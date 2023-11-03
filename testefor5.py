#progressão aritimética

a1 = float(input("Digite o primeiro termo da p.a:"))
razao = int(input("Digite a razão da p.a:"))

for i in range(10):
    termo = a1 + i * razao #formula 
    print(termo)

#se usar a = a1 + razao vai ta iterando sem atualizar o primeiro valor 