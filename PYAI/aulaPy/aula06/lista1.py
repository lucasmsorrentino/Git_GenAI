# Lista 1 - Exercicios de Strings
# Aula 06 - Manipulacao de Strings

import unicodedata


# --------------------------------------------------------
# 1. Comprimento da string
# --------------------------------------------------------
def comprimento(texto):
    contador = 0
    for _ in texto:
        contador += 1
    return contador


# --------------------------------------------------------
# 2. Inversao de string (sem usar [::-1])
# --------------------------------------------------------
def inverter(texto):
    resultado = ""
    for i in range(len(texto) - 1, -1, -1):
        resultado += texto[i]
    return resultado


# --------------------------------------------------------
# 3. Contagem de vogais e consoantes
# --------------------------------------------------------
def contar_vogais_consoantes(texto):
    vogais = 0
    consoantes = 0
    texto_norm = unicodedata.normalize('NFD', texto.lower())
    texto_norm = ''.join(c for c in texto_norm if unicodedata.category(c) != 'Mn')
    for c in texto_norm:
        if c.isalpha():
            if c in "aeiou":
                vogais += 1
            else:
                consoantes += 1
    return vogais, consoantes


# --------------------------------------------------------
# 4. Remocao de espacos extras
# --------------------------------------------------------
def remover_espacos_extras(texto):
    resultado = ""
    espaco_anterior = True
    for c in texto:
        if c == " ":
            if not espaco_anterior:
                resultado += c
            espaco_anterior = True
        else:
            resultado += c
            espaco_anterior = False
    if resultado.endswith(" "):
        resultado = resultado[:-1]
    return resultado


# --------------------------------------------------------
# 5. Verificador de palindromo
# --------------------------------------------------------
def eh_palindromo(texto):
    texto_norm = unicodedata.normalize('NFD', texto.lower())
    texto_norm = ''.join(c for c in texto_norm if unicodedata.category(c) != 'Mn')
    apenas_letras = ""
    for c in texto_norm:
        if c.isalnum():
            apenas_letras += c
    return apenas_letras == inverter(apenas_letras)


# --------------------------------------------------------
# 6. Tokenizacao simples
# --------------------------------------------------------
def tokenizar(frase):
    pontuacao = ".,!?;:"
    palavras = frase.split(" ")
    resultado = []
    for p in palavras:
        limpa = ""
        for c in p:
            if c not in pontuacao:
                limpa += c
        if limpa != "":
            resultado.append(limpa.lower())
    return resultado


# --------------------------------------------------------
# 7. Substituicao de caracteres (sem usar replace)
# --------------------------------------------------------
def substituir(texto, antigo, novo):
    resultado = ""
    for c in texto:
        if c == antigo:
            resultado += novo
        else:
            resultado += c
    return resultado


# --------------------------------------------------------
# 8. Extracao de iniciais
# --------------------------------------------------------
def iniciais(nome):
    partes = nome.split(" ")
    letras = []
    for p in partes:
        if p != "":
            letras.append(p[0].upper())
    return ".".join(letras)


# --------------------------------------------------------
# 9. Chunking de texto para LLM
# --------------------------------------------------------
def chunking(texto, n):
    chunks = []
    restante = texto
    while len(restante) > n:
        fatia = restante[:n]
        corte = fatia.rfind(" ")
        if corte == -1:
            corte = n
        chunks.append(restante[:corte].strip())
        restante = restante[corte:].strip()
    if restante:
        chunks.append(restante)
    return chunks


# --------------------------------------------------------
# 10. Contagem de frequencia de palavras
# --------------------------------------------------------
def frequencia_palavras(texto):
    pontuacao = ".,!?;:"
    limpo = ""
    for c in texto.lower():
        if c not in pontuacao:
            limpo += c
    palavras = limpo.split()
    frequencia = {}
    for p in palavras:
        if p in frequencia:
            frequencia[p] += 1
        else:
            frequencia[p] = 1
    return frequencia


# --------------------------------------------------------
# Testes
# --------------------------------------------------------
if __name__ == "__main__":
    print("1. Comprimento:", comprimento("Ola mundo"))

    print("2. Inversao:", inverter("Python"))

    v, c = contar_vogais_consoantes("GenAI")
    print(f"3. Vogais: {v}, Consoantes: {c}")

    print("4. Espacos:", repr(remover_espacos_extras("  Ola   mundo   da  IA  ")))

    print("5. Palindromo:", eh_palindromo("A man a plan a canal panama"))
    print("5. Palindromo:", eh_palindromo("Python"))

    print("6. Tokens:", tokenizar("Ola, como voce esta?"))

    print("7. Substituir:", substituir("banana", "a", "o"))

    print("8. Iniciais:", iniciais("ana maria silva"))

    texto_chunk = "Este e um exemplo de chunking para modelos generativos"
    print("9. Chunks:", chunking(texto_chunk, 20))

    print("10. Frequencia:", frequencia_palavras(
        "O rato roeu a roupa do rei de Roma. O rei ficou bravo."
    ))
