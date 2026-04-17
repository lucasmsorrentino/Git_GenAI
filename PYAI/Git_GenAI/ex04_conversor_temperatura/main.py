# EX. 4: Conversor de Temperatura
# Converte Celsius para Fahrenheit: (C × 9/5) + 32

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit:.2f}°F")
