# EX. 3: Par ou Ímpar
# Peça um número e diga se ele é par ou ímpar.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"{numero} é PAR.")
else:
    print(f"{numero} é ÍMPAR.")
