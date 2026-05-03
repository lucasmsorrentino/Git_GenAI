# Projeto: Identificador de Idioma por Frequencia de Letras
# Aula 06 - Strings
#
# Baixa o texto de uma URL, calcula a frequencia relativa das letras
# (incluindo caracteres com acento e cedilha) e compara com perfis
# pre-carregados de pt, en, es usando duas metricas: distancia
# euclidiana e similaridade do cosseno.
#
# Referencias dos perfis de frequencia de letras:
# - Wikipedia (Letter frequency, ingles):
#   https://en.wikipedia.org/wiki/Letter_frequency
# - Wikipedia (Frequencia de letras, portugues):
#   https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras
# - Wikipedia (Frecuencia de aparicion de letras, espanhol):
#   https://es.wikipedia.org/wiki/Frecuencia_de_aparici%C3%B3n_de_letras
# Os valores das letras com acento sao aproximados a partir dessas
# tabelas e de literatura de referencia em cada idioma.

import math
import unicodedata
import requests


# Alfabeto: 26 letras a-z mais os caracteres com acento e cedilha
# tipicos dos idiomas analisados (mantidos como letras distintas).
ALFABETO = (
    "abcdefghijklmnopqrstuvwxyz"
    "áâãàç"
    "éê"
    "í"
    "óôõ"
    "ú"
    "ñü"
)


PERFIS = {
    "portugues": {
        "a": 12.20, "á": 0.50, "â": 0.10, "ã": 1.80, "à": 0.03,
        "b": 1.04,
        "c": 3.38, "ç": 0.50,
        "d": 4.99,
        "e": 10.97, "é": 1.30, "ê": 0.30,
        "f": 1.02, "g": 1.30, "h": 1.28,
        "i": 5.68, "í": 0.50,
        "j": 0.40, "k": 0.02, "l": 2.78, "m": 4.74, "n": 5.05,
        "o": 9.20, "ó": 0.95, "ô": 0.40, "õ": 0.18,
        "p": 2.52, "q": 1.20, "r": 6.53, "s": 7.81, "t": 4.34,
        "u": 4.40, "ú": 0.23,
        "v": 1.67, "w": 0.01, "x": 0.21, "y": 0.01, "z": 0.47,
        "ñ": 0.00, "ü": 0.00,
    },
    "ingles": {
        "a": 8.17, "á": 0.00, "â": 0.00, "ã": 0.00, "à": 0.00,
        "b": 1.49,
        "c": 2.78, "ç": 0.00,
        "d": 4.25,
        "e": 12.70, "é": 0.00, "ê": 0.00,
        "f": 2.23, "g": 2.02, "h": 6.09,
        "i": 6.97, "í": 0.00,
        "j": 0.15, "k": 0.77, "l": 4.03, "m": 2.41, "n": 6.75,
        "o": 7.51, "ó": 0.00, "ô": 0.00, "õ": 0.00,
        "p": 1.93, "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06,
        "u": 2.76, "ú": 0.00,
        "v": 0.98, "w": 2.36, "x": 0.15, "y": 1.97, "z": 0.07,
        "ñ": 0.00, "ü": 0.00,
    },
    "espanhol": {
        "a": 11.03, "á": 0.50, "â": 0.00, "ã": 0.00, "à": 0.00,
        "b": 2.22,
        "c": 4.02, "ç": 0.00,
        "d": 5.01,
        "e": 11.78, "é": 0.40, "ê": 0.00,
        "f": 0.69, "g": 1.77, "h": 0.70,
        "i": 5.55, "í": 0.70,
        "j": 0.49, "k": 0.01, "l": 4.97, "m": 3.16,
        "n": 6.41, "ñ": 0.30,
        "o": 7.88, "ó": 0.80, "ô": 0.00, "õ": 0.00,
        "p": 2.51, "q": 0.88, "r": 6.87, "s": 7.98, "t": 4.63,
        "u": 2.72, "ú": 0.20,
        "v": 1.14, "w": 0.02, "x": 0.22, "y": 1.01, "z": 0.47,
        "ü": 0.01,
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
    # Converte para minusculas e mantem apenas os caracteres do ALFABETO
    # (a-z e os acentos/cedilha previstos). NFC normaliza acentos que
    # podem vir decompostos no HTML (ex.: "e" + combining acute).
    texto = remover_tags_html(texto)
    texto = texto.lower()
    texto = unicodedata.normalize('NFC', texto)
    resultado = ""
    for c in texto:
        if c in ALFABETO:
            resultado += c
    return resultado


def calcular_frequencia(texto_limpo):
    # Calcula o percentual de cada letra (do ALFABETO) no texto limpo.
    frequencia = {}
    for letra in ALFABETO:
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
    # Mede o "tamanho" do vetor de diferenca entre dois perfis.
    # Quanto menor, mais parecidos. Minimo 0, sem limite superior.
    soma = 0.0
    for letra in ALFABETO:
        diferenca = freq_a.get(letra, 0) - freq_b.get(letra, 0)
        soma += diferenca ** 2
    return math.sqrt(soma)


def similaridade_cosseno(freq_a, freq_b):
    # Mede o cosseno do angulo entre dois vetores de frequencia.
    # 1.0 = perfis identicos em direcao; 0.0 = totalmente diferentes.
    # Naturalmente normalizado entre 0 e 1 quando as entradas sao >= 0.
    produto = 0.0
    norma_a = 0.0
    norma_b = 0.0
    for letra in ALFABETO:
        a = freq_a.get(letra, 0)
        b = freq_b.get(letra, 0)
        produto += a * b
        norma_a += a * a
        norma_b += b * b
    if norma_a == 0 or norma_b == 0:
        return 0.0
    return produto / (math.sqrt(norma_a) * math.sqrt(norma_b))


def comparar_perfis(freq_texto, perfis):
    # Retorna lista de dicts {idioma, distancia, sim_euc, cosseno, sim_cos}
    # com o resultado de cada idioma nas duas metricas.
    resultados = []
    for idioma, perfil in perfis.items():
        dist = distancia_euclidiana(freq_texto, perfil)
        cos = similaridade_cosseno(freq_texto, perfil)
        resultados.append({
            "idioma": idioma,
            "distancia": dist,
            "sim_euc": max(0.0, 100.0 - dist),
            "cosseno": cos,
            "sim_cos": cos * 100.0,
        })
    return resultados


def imprimir_tabela(resultados):
    # Imprime a tabela com a pontuacao de cada idioma nas duas metricas.
    print(f"  {'idioma':<10} {'distancia':>10} {'sim. eucl.':>11} "
          f"{'cosseno':>10} {'sim. cos.':>10}")
    print(f"  {'-'*10} {'-'*10} {'-'*11} {'-'*10} {'-'*10}")
    for r in resultados:
        print(f"  {r['idioma']:<10} {r['distancia']:10.3f} "
              f"{r['sim_euc']:10.2f}% {r['cosseno']:10.4f} "
              f"{r['sim_cos']:9.2f}%")


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
    resultados = comparar_perfis(freq, perfis)

    # Vencedores por metrica.
    melhor_euc = min(resultados, key=lambda r: r["distancia"])
    melhor_cos = max(resultados, key=lambda r: r["cosseno"])

    print(f"URL: {url}")
    print(f"Letras analisadas: {len(limpo)}")
    print()
    print("Pontuacao por idioma:")
    imprimir_tabela(resultados)
    print()
    print(f"Distancia euclidiana: o texto esta em {melhor_euc['idioma']} "
          f"com grau de similaridade {melhor_euc['sim_euc']:.2f}% "
          f"(distancia={melhor_euc['distancia']:.2f}).")
    print(f"Similaridade do cosseno: o texto esta em {melhor_cos['idioma']} "
          f"com grau de similaridade {melhor_cos['sim_cos']:.2f}% "
          f"(cosseno={melhor_cos['cosseno']:.4f}).")


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
