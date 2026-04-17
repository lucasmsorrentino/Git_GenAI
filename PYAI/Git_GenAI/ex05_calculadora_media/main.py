# EX. 5: Calculadora de Média
# Peça 4 notas, calcule a média e diga se o aluno foi aprovado ou reprovado.

notas = []
for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"\nMédia: {media:.2f}")
if media >= 7:
    print("Resultado: APROVADO!")
else:
    print("Resultado: REPROVADO.")
