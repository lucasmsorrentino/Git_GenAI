from typing import cast


class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self._cpf = cpf

    def __eq__(self, other):
        return self._cpf == cast(Pessoa, other)._cpf


def main():
    p1 = Pessoa("João", 33333333333)
    p2 = Pessoa("João", 11111111111)

    if p1 == p2:
        print("Pessoas Iguais")
    else:
        print("Pessoas Diferentes")


if __name__ == "__main__":
    main()