# EX. 2: Calculadora de Soma
# Peça dois números e mostre a soma, subtração, multiplicação e divisão.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"Soma:         {a + b:g}")
print(f"Subtração:    {a - b:g}")
print(f"Multiplicação:{a * b:g}")
print(f"Divisão:      {a / b:g}" if b != 0 else "Divisão:      indefinida (divisão por zero)")
