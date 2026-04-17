# EX. 8: Contador de Vogais
# Peça uma palavra ou frase e conte vogais e consoantes.

texto = input("Digite uma palavra ou frase: ").lower()

vogais = "aeiouáéíóúàèìòùãõâêîôû"
qtd_vogais = 0
qtd_consoantes = 0

for char in texto:
    if char.isalpha():
        if char in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1

print(f"Vogais:     {qtd_vogais}")
print(f"Consoantes: {qtd_consoantes}")
