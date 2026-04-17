# EX. 14: Analisador de Texto
# Mostra: total de caracteres, número de palavras, palavra mais longa e frequência de letras.

texto = input("Digite um texto: ")

palavras = texto.split()
palavra_mais_longa = max(palavras, key=len) if palavras else ""

frequencia = {}
for char in texto.lower():
    if char.isalpha():
        frequencia[char] = frequencia.get(char, 0) + 1

print(f"\nTotal de caracteres: {len(texto)}")
print(f"Número de palavras:  {len(palavras)}")
print(f"Palavra mais longa:  {palavra_mais_longa}")
print("Frequência de letras:")
for letra, qtd in sorted(frequencia.items()):
    print(f"  {letra}: {qtd}")
