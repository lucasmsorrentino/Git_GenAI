#Considere a classe a seguir:

class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError("Idade precisa ser maior ou igual a zero")
        self._idade = idade


try:
    print("Instanciando")
    a = Animal("Meu Cachorro", 5)
    print("Animal criado na memória")
    a.idade = -3
    print("A idade é", a.idade)

except Exception as e:
    print(e)