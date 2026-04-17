# EX. 12: Fibonacci
# Mostre os primeiros N números da sequência de Fibonacci.

n = int(input("Quantos números de Fibonacci deseja ver? "))

a, b = 0, 1
print("Sequência de Fibonacci:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
