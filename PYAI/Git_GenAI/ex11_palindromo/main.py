# EX. 11: Palíndromo
# Verifique se uma palavra é um palíndromo (lê igual de trás para frente).

palavra = input("Digite uma palavra: ").strip().lower()
invertida = palavra[::-1]

if palavra == invertida:
    print(f'"{palavra}" É um palíndromo.')
else:
    print(f'"{palavra}" NÃO é um palíndromo.')
