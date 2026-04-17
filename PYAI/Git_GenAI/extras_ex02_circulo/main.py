# Exercícios Extras - Ex. 2: Círculo
# Solicita o raio e exibe o perímetro e a área do círculo.

import math

raio = float(input("Digite o raio do círculo: "))

perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

print(f"Perímetro: {perimetro:.4f}")
print(f"Área: {area:.4f}")
