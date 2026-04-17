# Desafio 2: Simulador de Caixa Eletrônico
# Entrega cédulas de 100, 50, 20 e 10.

cedulas = [100, 50, 20, 10]

valor = int(input("Digite o valor a sacar (múltiplo de 10): "))

if valor <= 0 or valor % 10 != 0:
    print("Valor inválido. Digite um múltiplo de 10 maior que zero.")
else:
    restante = valor
    resultado = {}

    for cedula in cedulas:
        quantidade = restante // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
            restante -= cedula * quantidade

    if restante == 0:
        print(f"\nSaque de R$ {valor}:")
        for cedula, qtd in resultado.items():
            print(f"  {qtd}x R$ {cedula}")
    else:
        print("Não foi possível realizar o saque com as cédulas disponíveis.")
