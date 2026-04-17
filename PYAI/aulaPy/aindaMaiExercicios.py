#EX. 1: Hello World Personalizado

# Peça o nome do usuário e imprima uma mensagem de boas-vindas personalizada
nome = input("Digite seu nome: ")

# Exemplo: "Olá, André! Seja bem-vinda à Especialização em IA Generativa!"
print(f"Olá, {nome}! Seja bem-vinda à Especialização em IA Generativa!")


#EX. 2: Calculadora de Soma
#Conceitos: Tipos numéricos, conversão de tipos

# Peça dois números ao usuário e mostre a soma deles
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}")

# Desafio: Mostre também a subtração, multiplicação e divisão
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Indefinida (divisão por zero)"
print(f"A subtração de {num1} e {num2} é {subtracao}")
print(f"A multiplicação de {num1} e {num2} é {multiplicacao}")
print(f"A divisão de {num1} e {num2} é {divisao}")


#EX. 3: Par ou Ímpar
#Conceitos: Operador "%" (módulo), condicionais "if/else"

# Peça um número ao usuário e informe se ele é par ou ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

#EX. 4: Conversor de Temperatura
#Conceitos: Operações matemáticas, formatação de strings

# Converta Celsius para Fahrenheit: (C × 9/5) + 32
# Peça a temperatura em Celsius e mostre em Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F.")
