import random

matriz = []
for i in range(3):
    l = []
    while len(l) < 3:
        l.append(random.randint(1, 10))
    matriz.append(l)

print(matriz)


soma = 0
for l in matriz:
    for c in l:
        soma += c

print(soma)

somafirstline = 0
for c in matriz[0]:
    somafirstline += c
print(somafirstline)

somaMainDiagonal = 0
for i in range(len(matriz)):
    somaMainDiagonal += matriz[i][i]
print(somaMainDiagonal)
