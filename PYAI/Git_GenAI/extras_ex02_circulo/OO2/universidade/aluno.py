from .pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome=None, cpf=-1, matricula=None, curso=None):
        super().__init__(nome, cpf)
        self._matricula = matricula
        self._curso = curso

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso
