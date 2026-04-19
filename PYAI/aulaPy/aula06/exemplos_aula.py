# Exemplos da Aula 06 - Manipulacao de Strings e Arquivos
# Replicando os exemplos mostrados nos slides

print("=" * 50)
print("STRINGS - Exemplos basicos")
print("=" * 50)

# Declaracao de strings
nome = "Maria Silva"
print(nome)

# len() - tamanho da string
frase = "Curso de Python"
print("Num caracs", len(frase))

# Acessando itens por indice
frase = "Curso de Python"
linguagem = frase[9:len(frase)]
print(linguagem)
print("Primeira Letra:", frase[0])

# replace()
frase = "Esse e o curso de IA Generativa. Voce pode criar programas com prompts."
mudanca = frase.replace("prompts", "Python")
print(frase)
print(mudanca)

# replace com limite de substituicoes
somente_prim = frase.replace("prompts", "Python", 1)
print(somente_prim)

# Concatenacao
nome_curso = "Python"
ola = "Bom dia."
frase = ola + " Esse e o curso de " + nome_curso + "."
print(frase)

# Caracteres de controle
frase = "Esse e um texto\nde\texemplo"
print(frase)

# Caixa: upper, lower, capitalize
frase1 = "CURSO de Python"
print(frase1.upper())
print(frase1.lower())
print(frase1.capitalize())

# Split
frase = "Esse e o curso de Python - Foco em iniciantes"
lista1 = frase.split(" ")
for item in lista1:
    print(item)

lista2 = frase.split("-")
for item in lista2:
    print(item)

# find()
frase = "Ola mundo teste isso vai ficar teste final"
inicio = frase.find("teste") + len("teste")
fim = frase.find("teste", inicio)
print(frase[inicio:fim])


print("=" * 50)
print("FORMATACAO DE STRINGS")
print("=" * 50)

# Usando format()
anterior = 5000
atual = 5500
diferenca = atual - anterior
pct = diferenca / anterior * 100
frase = "A diferenca de salario e de R${}, ou seja, {}%"
formatado = frase.format(diferenca, pct)
print(formatado)

# Formatando diretamente no print
salario = 7500
print("O seu salario e {}.".format(salario))

# Format e tipos (float)
print("O seu salario e {:f}.".format(salario))

# Limitando casas decimais
print("O seu salario e {:.2f}.".format(salario))


print("=" * 50)
print("ARQUIVOS - Escrita e Leitura")
print("=" * 50)

# Escrita - exemplo do slide
valor = 10
pi = 3.14
nome = "Maria da Silva"

arq = open("documento.txt", "w")
arq.write(str(valor))
arq.write(';')
arq.write(str(pi))
arq.write(';')
arq.write(nome)
arq.write('\n')
arq.close()

# Leitura com read()
arq = open("documento.txt", "r")
conteudo = arq.read()
print("Conteudo lido com read():")
print(conteudo)
arq.close()

# Leitura com readline()
arq = open("documento.txt", "r")
conteudo = arq.readline()
while conteudo != "":
    print("Linha lida:", conteudo, end="")
    conteudo = arq.readline()
arq.close()

# Iterando linha a linha
arq = open("documento.txt", "r")
for linha in arq:
    print("Linha lida:", linha, end="")
arq.close()


print("=" * 50)
print("ARQUIVO CSV - Exemplo")
print("=" * 50)

# Criando um CSV exemplo para testar
arq = open("exemplo.csv", "w")
arq.write("Nome;Idade;Salario\n")
arq.write("Maria Silva;45;8500,85\n")
arq.write("Jose Oliveira;30;5500,4\n")
arq.write("Marcos Santos;35;8000\n")
arq.close()

# Lendo CSV "no braco"
arq = open("exemplo.csv", "r")
arq.readline()  # descartando primeira linha (cabecalho)

idades = 0
salarios = 0
qtde = 0
for linha in arq:
    quebra = linha.split(';')
    idades = idades + int(quebra[1])
    salarios = salarios + float(quebra[2].replace(',', '.'))
    qtde = qtde + 1
arq.close()

print("A idade media e", idades / qtde)
print("O salario medio e", salarios / qtde)

# Lendo CSV com a biblioteca csv
import csv

arq = open("exemplo.csv", "r")
csv_reader = csv.reader(arq, delimiter=';')
next(csv_reader)  # pular a primeira linha

idades = 0
salarios = 0
qtde = 0
for linha in csv_reader:
    idades = idades + int(linha[1])
    salarios = salarios + float(linha[2].replace(',', '.'))
    qtde = qtde + 1
arq.close()

print("[csv lib] A idade media e", idades / qtde)
print("[csv lib] O salario medio e", salarios / qtde)
