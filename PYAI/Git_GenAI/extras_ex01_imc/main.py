# Exercícios Extras - Ex. 1: IMC
# Pergunte o peso (kg) e a altura (m) e calcule o IMC = peso / (altura * altura)

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")
