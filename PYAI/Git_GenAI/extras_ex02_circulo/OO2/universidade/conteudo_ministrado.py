class ConteudoMinistrado:
    def __init__(self, nome, carga_horaria=0):
        self._nome = nome
        self._carga_horaria = carga_horaria

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
