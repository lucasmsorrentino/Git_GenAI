# 1. Considere um arquivo de texto a ser passado pelo usuário via argumento na linha de comando:
# a. Crie um contador de palavras onde cada palavra é uma chave em um dicionário e a frequência de ocorrência é o valor a se
# armazenar na chave.
# b. Crie um contador de caracteres (todos, incluindo sinais de pontuação e espaço) que mostre, ao final, o número total de caracteres do
# texto e a frequência individual de cada um (use um dicionário).
# c. Imprima o dicionário de palavras em ordem alfabética inversa (de Z para A)
# d. Imprima o dicionário de caracteres em ordem alfabética

import sys

def contar_palavras_e_caracteres(arquivo):
    contador_palavras = {}
    contador_caracteres = {}

    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            for palavra in linha.split():
                palavra = palavra.lower()  # Normaliza para minúsculas
                contador_palavras[palavra] = contador_palavras.get(palavra, 0) + 1

            for caractere in linha:
                contador_caracteres[caractere] = contador_caracteres.get(caractere, 0) + 1

    return contador_palavras, contador_caracteres

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python dict.py <arquivo>")
        sys.exit(1)

    arquivo = sys.argv[1]
    palavras, caracteres = contar_palavras_e_caracteres(arquivo)

    print("Dicionário de palavras (ordem alfabética inversa):")
    for palavra in sorted(palavras.keys(), reverse=True):
        print(f"{palavra}: {palavras[palavra]}")

    print("\nDicionário de caracteres (ordem alfabética):")
    for caractere in sorted(caracteres.keys()):
        print(f"{caractere}: {caracteres[caractere]}")

