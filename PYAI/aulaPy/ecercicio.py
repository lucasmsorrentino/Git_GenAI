# exercicio 01
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
imc=peso/(altura*altura)

print("Seu imc é", imc)

# exercicio 02
import math
raio=float(input("Digite o raio do círculo: ")) 

print("A área do círculo é", math.pi * raio**2)

# exercicio 03

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print("Raíz 1:", x1)
print("Raíz 2:", x2)