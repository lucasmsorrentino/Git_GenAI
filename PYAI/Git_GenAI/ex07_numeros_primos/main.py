# EX. 7: Números Primos
# Peça um número e diga se ele é primo ou não.

numero = int(input("Digite um número inteiro positivo: "))

if numero < 2:
    print(f"{numero} NÃO é primo.")
else:
    primo = True
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            primo = False
            break
        i += 1

    if primo:
        print(f"{numero} É primo.")
    else:
        print(f"{numero} NÃO é primo.")
