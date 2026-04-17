from .professor import Professor


class Disciplina:
    def __init__(self, nome, carga_horaria=60, professor=None):
        self._nome = nome
        self.carga_horaria = carga_horaria
        self.professor = professor
        self._conteudos_ministrados = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def carga_horaria(self):
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self._carga_horaria = carga_horaria

    @property
    def professor(self):
        return self._professor

    @professor.setter
    def professor(self, professor):
        if professor is not None and not issubclass(type(professor), Professor):
            raise TypeError("parâmetro professor deve derivar da classe Professor")
        self._professor = professor

    @property
    def conteudos_ministrados(self):
        return tuple(self._conteudos_ministrados)

    def adicionar_conteudo(self, conteudo):
        self._conteudos_ministrados.append(conteudo)
