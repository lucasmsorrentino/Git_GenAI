# Identificador de Idioma por Frequência de Letras

Projeto da aula 06 - Strings. Baixa o conteúdo de uma URL, calcula a
frequência relativa das letras do texto e compara com perfis conhecidos
de português, inglês e espanhol para identificar o idioma mais provável.

## Como executar

```bash
pip install requests
python3 identificador_idioma.py
```

Digite a URL quando solicitado. Exemplos:

- `https://pt.wikipedia.org/wiki/Python` (português)
- `https://en.wikipedia.org/wiki/Python_(programming_language)` (inglês)
- `https://es.wikipedia.org/wiki/Python` (espanhol)

## Como funciona

1. `baixar_texto(url)` - obtém o HTML da página via `requests`.
2. `limpar_texto(texto)` - remove tags HTML, converte para minúsculas,
   remove acentos via `unicodedata` e mantém apenas letras a-z.
3. `calcular_frequencia(texto)` - retorna o percentual de cada letra.
4. `carregar_perfis()` - retorna um dicionário com as frequências
   esperadas de cada idioma (valores de referência da literatura).
5. `comparar_perfis(freq, perfis)` - calcula a distância euclidiana
   entre o perfil do texto e cada idioma, retornando o mais próximo.
