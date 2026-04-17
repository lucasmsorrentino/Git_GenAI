# Exercícios Extras - Ex. 3: Bhaskara
# Lê os coeficientes a, b, c e calcula as raízes da equação de 2º grau.

import math

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

delta = b ** 2 - 4 * a * c

raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"Raíz 1: {raiz1:g}")
print(f"Raíz 2: {raiz2:g}")
