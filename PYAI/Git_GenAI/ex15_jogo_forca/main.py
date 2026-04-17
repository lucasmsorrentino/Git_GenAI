# EX. 15: Jogo da Forca
# Palavra secreta, underscores, palpites de letras, controle de tentativas erradas.

import random

palavras = ["python", "programacao", "computador", "algoritmo", "variavel", "funcao"]
palavra = random.choice(palavras)
letras_descobertas = set()
letras_erradas = set()
max_erros = 6

print("=== Jogo da Forca ===")

while True:
    # Mostrar estado atual
    display = " ".join(letra if letra in letras_descobertas else "_" for letra in palavra)
    print(f"\nPalavra: {display}")
    print(f"Erros ({len(letras_erradas)}/{max_erros}): {' '.join(sorted(letras_erradas))}")

    # Verificar vitória
    if all(letra in letras_descobertas for letra in palavra):
        print(f"\nParabéns! Você acertou a palavra: {palavra}")
        break

    # Verificar derrota
    if len(letras_erradas) >= max_erros:
        print(f"\nVocê perdeu! A palavra era: {palavra}")
        break

    palpite = input("Digite uma letra: ").strip().lower()
    if len(palpite) != 1 or not palpite.isalpha():
        print("Digite apenas uma letra.")
        continue

    if palpite in letras_descobertas or palpite in letras_erradas:
        print("Você já tentou essa letra.")
        continue

    if palpite in palavra:
        letras_descobertas.add(palpite)
        print("Acertou!")
    else:
        letras_erradas.add(palpite)
        print("Errou!")
