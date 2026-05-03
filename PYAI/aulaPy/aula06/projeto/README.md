# Identificador de Idioma por Frequência de Letras

Projeto da aula 06 - Strings. Baixa o conteúdo de uma URL, calcula a
frequência relativa das letras do texto (incluindo acentos e cedilha)
e compara com perfis conhecidos de português, inglês e espanhol para
identificar o idioma mais provável.

## Como executar

```bash
pip install requests
python identificador_idioma.py
```

Digite a URL quando solicitado. Exemplos com texto bem representativo
de cada idioma:

- `https://pt.wikipedia.org/wiki/Machado_de_Assis` (português)
- `https://en.wikipedia.org/wiki/William_Shakespeare` (inglês)
- `https://es.wikipedia.org/wiki/Don_Quijote_de_la_Mancha` (espanhol)


## Como funciona

1. `baixar_texto(url)` - obtém o HTML da página via `requests`.
2. `limpar_texto(texto)` - remove tags HTML, converte para minúsculas,
   normaliza Unicode (NFC) e mantém apenas os caracteres do alfabeto
   considerado: `a-z` mais os acentos/cedilha relevantes
   (`á â ã à ç é ê í ó ô õ ú ñ ü`).
3. `calcular_frequencia(texto)` - retorna o percentual de cada letra.
4. `carregar_perfis()` - retorna um dicionário com as frequências
   esperadas de cada idioma (valores de referência da literatura).
5. `comparar_perfis(freq, perfis)` - calcula **duas métricas** de
   similaridade contra cada idioma e retorna o mais provável segundo
   cada uma.

## Métricas usadas

### Distância euclidiana

Mede o "tamanho" do vetor de diferenças entre os dois perfis:

`d(A, B) = sqrt( Σ (a_i - b_i)² )`

Quanto menor, mais parecidos. Para apresentar como percentual usamos
`100 - distância`.

### Similaridade do cosseno

Mede o cosseno do ângulo entre os dois vetores de frequência:

`cos(θ) = (A · B) / (||A|| × ||B||)`

Já vem normalizada entre 0 e 1 (quando as frequências são ≥ 0), o que
torna o percentual diretamente interpretável. É a métrica padrão em
NLP e usada em embeddings de LLMs.

## Por que considerar caracteres especiais?

O PDF do projeto deixa em aberto a decisão de manter ou remover acentos
e cedilha. Optamos por **manter** (`á â ã à ç é ê í ó ô õ ú ñ ü` como
letras distintas) porque eles trazem sinal forte para discriminar
idiomas latinos:

- **ç**: aparece em PT, ausente em EN/ES.
- **ã, õ, ô**: praticamente exclusivos do PT.
- **ñ**: praticamente exclusivo do ES.

Para validar a escolha, rodamos o programa nas mesmas 6 URLs com as
duas abordagens — **com** acentos/cedilha (versão final) e **sem**
(mapeando `ã→a, ç→c, ñ→n` etc., só `a-z`):

| Métrica | Com especiais | Sem especiais |
|---|---|---|
| Distância euclidiana | **6/6** ✓ | 5/6 |
| Similaridade do cosseno | **6/6** ✓ | 5/6 |

O caso que falha sem especiais é a página `Língua portuguesa`, que vai
para `espanhol` por uma diferença mínima — PT e ES têm distribuição
muito parecida em `a-z`, e os acentos/cedilha são justamente o
desempate. Para textos em inglês não há diferença prática (inglês não
usa diacríticos com frequência relevante).

## Referências dos perfis de frequência

- Wikipedia — *Letter frequency* (inglês):
  <https://en.wikipedia.org/wiki/Letter_frequency>
- Wikipedia — *Frequência de letras* (português):
  <https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras>
- Wikipedia — *Frecuencia de aparición de letras* (espanhol):
  <https://es.wikipedia.org/wiki/Frecuencia_de_aparici%C3%B3n_de_letras>

Os valores das letras com acento foram aproximados a partir das
tabelas acima e de literatura de referência em cada idioma.
