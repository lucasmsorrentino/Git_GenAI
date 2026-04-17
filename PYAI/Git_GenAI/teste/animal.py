class Animal:
    def __init__(self):
        print("Inicializado o animal")
        self.__nome = None

    @property
    def nome(self):
        print("Getter acionado")
        return self.__nome

    @nome.setter
    def nome(self, nome):
        print("Setter acionado")
        self.__nome = nome

    def set_nome(self, nome):
        print("Função secundária acionada")
        self.__nome = nome

# Considere que o seguinte foi feito no main.py


animal = Animal()
animal.nome = "Meu Cachorro"

nome = animal.nome
print(nome)