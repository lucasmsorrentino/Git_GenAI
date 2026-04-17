# EX. 6: Tabuada
# Peça um número e mostre a tabuada dele de 1 a 10.

numero = int(input("Digite um número: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
