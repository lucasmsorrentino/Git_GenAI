# EX. 9: Jogo da Adivinhação
# Gere um número aleatório entre 1 e 100 e peça ao usuário adivinhar.

import random

secreto = random.randint(1, 100)
tentativas = 0

print("Adivinhe o número entre 1 e 100!")

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite < secreto:
        print("Maior!")
    elif palpite > secreto:
        print("Menor!")
    else:
        print(f"Acertou! O número era {secreto}. Tentativas: {tentativas}")
        break
