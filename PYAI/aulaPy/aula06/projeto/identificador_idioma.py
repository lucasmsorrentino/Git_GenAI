# Projeto: Identificador de Idioma por Frequencia de Letras
# Aula 06 - Strings
#
# Baixa o texto de uma URL, calcula a frequencia relativa das letras
# e compara com perfis pre-carregados de varios idiomas (pt, en, es)
# usando distancia euclidiana. Retorna o idioma mais provavel.

import math
import unicodedata
import requests


# Perfis de frequencia de letras (em %) baseados em literatura classica.
# Fonte: valores aproximados de referencia (Wikipedia - Letter frequency).
PERFIS = {
    "portugues": {
        "a": 14.63, "b": 1.04, "c": 3.88, "d": 4.99, "e": 12.57,
        "f": 1.02, "g": 1.30, "h": 1.28, "i": 6.18, "j": 0.40,
        "k": 0.02, "l": 2.78, "m": 4.74, "n": 5.05, "o": 10.73,
        "p": 2.52, "q": 1.20, "r": 6.53, "s": 7.81, "t": 4.34,
        "u": 4.63, "v": 1.67, "w": 0.01, "x": 0.21, "y": 0.01,
        "z": 0.47,
    },
    "ingles": {
        "a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.70,
        "f": 2.23, "g": 2.02, "h": 6.09, "i": 6.97, "j": 0.15,
        "k": 0.77, "l": 4.03, "m": 2.41, "n": 6.75, "o": 7.51,
        "p": 1.93, "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06,
        "u": 2.76, "v": 0.98, "w": 2.36, "x": 0.15, "y": 1.97,
        "z": 0.07,
    },
    "espanhol": {
        "a": 11.96, "b": 0.92, "c": 2.92, "d": 6.87, "e": 16.78,
        "f": 0.52, "g": 0.73, "h": 0.89, "i": 4.15, "j": 0.30,
        "k": 0.00, "l": 8.37, "m": 2.12, "n": 7.01, "o": 8.69,
        "p": 2.76, "q": 1.53, "r": 4.94, "s": 7.88, "t": 3.31,
        "u": 4.80, "v": 0.39, "w": 0.01, "x": 0.06, "y": 1.54,
        "z": 0.15,
    },
}


def baixar_texto(url):
    # Baixa o conteudo textual de uma URL. Retorna string ou None em caso de erro.
    headers = {
        "User-Agent": "Mozilla/5.0 (IdentificadorIdioma/1.0) Python/requests"
    }
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
        return resposta.text
    except requests.exceptions.RequestException as erro:
        print(f"Erro ao baixar {url}: {erro}")
        return None


def remover_tags_html(texto):
    # Remove tags HTML de forma simples, substituindo-as por espaco.
    resultado = ""
    dentro_tag = False
    for c in texto:
        if c == "<":
            dentro_tag = True
        elif c == ">":
            dentro_tag = False
            resultado += " "
        elif not dentro_tag:
            resultado += c
    return resultado


def limpar_texto(texto):
    # Converte para minusculas, remove acentos, mantem apenas letras a-z.
    texto = remover_tags_html(texto)
    texto = texto.lower()
    texto_norm = unicodedata.normalize('NFD', texto)
    texto_sem_acento = ""
    for c in texto_norm:
        if unicodedata.category(c) != 'Mn':
            texto_sem_acento += c
    resultado = ""
    for c in texto_sem_acento:
        if 'a' <= c <= 'z':
            resultado += c
    return resultado


def calcular_frequencia(texto_limpo):
    # Calcula o percentual de cada letra no texto limpo.
    frequencia = {}
    for letra in "abcdefghijklmnopqrstuvwxyz":
        frequencia[letra] = 0
    total = len(texto_limpo)
    if total == 0:
        return frequencia
    for c in texto_limpo:
        frequencia[c] += 1
    for letra in frequencia:
        frequencia[letra] = (frequencia[letra] / total) * 100
    return frequencia


def carregar_perfis():
    # Retorna os perfis de referencia definidos como constante.
    return PERFIS


def distancia_euclidiana(freq_a, freq_b):
    soma = 0.0
    for letra in "abcdefghijklmnopqrstuvwxyz":
        diferenca = freq_a.get(letra, 0) - freq_b.get(letra, 0)
        soma += diferenca ** 2
    return math.sqrt(soma)


def comparar_perfis(freq_texto, perfis):
    # Retorna (idioma_mais_proximo, distancia, similaridade_percentual).
    melhor_idioma = None
    menor_distancia = float('inf')
    for idioma, perfil in perfis.items():
        dist = distancia_euclidiana(freq_texto, perfil)
        if dist < menor_distancia:
            menor_distancia = dist
            melhor_idioma = idioma
    # Transforma a distancia em uma "similaridade" amigavel (0-100%).
    # Distancia 0 = 100%; cresce negativamente conforme afasta.
    similaridade = max(0.0, 100.0 - menor_distancia)
    return melhor_idioma, menor_distancia, similaridade


def identificar(url):
    texto = baixar_texto(url)
    if texto is None:
        return
    limpo = limpar_texto(texto)
    if len(limpo) == 0:
        print("Nao foi possivel extrair texto util da pagina.")
        return
    freq = calcular_frequencia(limpo)
    perfis = carregar_perfis()
    idioma, distancia, similaridade = comparar_perfis(freq, perfis)
    print(f"URL: {url}")
    print(f"Letras analisadas: {len(limpo)}")
    print(f"O texto esta em {idioma} com grau de similaridade {similaridade:.2f}% "
          f"(distancia={distancia:.2f}).")


def main():
    print("Identificador de Idioma por Frequencia de Letras")
    print("-" * 50)
    url = input("Informe a URL: ").strip()
    if url == "":
        print("URL vazia. Encerrando.")
        return
    identificar(url)


if __name__ == "__main__":
    main()
