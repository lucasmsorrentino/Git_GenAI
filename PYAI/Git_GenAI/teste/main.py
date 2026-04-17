class MinhaClasse:
    A = 10

    def __init__(self, valor):
        self.b = valor
        MinhaClasse.A = valor


# O que será impresso na tela, considerando o seguinte trecho no arquivo main.py?


mc1 = MinhaClasse(1)
mc2 = MinhaClasse(2)
mc3 = MinhaClasse(3)

print(mc1.A, mc1.b)
print(mc2.A, mc2.b)
print(mc3.A, mc3.b)