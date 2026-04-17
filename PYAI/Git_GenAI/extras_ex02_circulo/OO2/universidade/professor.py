from abc import ABC, abstractmethod

from .pessoa import Pessoa


class Professor(ABC, Pessoa):
    def __init__(self, nome, cpf, valor_hora=60, carga_horaria=40):
        super().__init__(nome, cpf)
        self._valor_hora = valor_hora
        self._carga_horaria = carga_horaria

    @property
    def valor_hora(self):
        return self._valor_hora

    @valor_hora.setter
    def valor_hora(self, valor_hora):
        self._valor_hora = valor_hora

    @property
    def carga_horaria(self):
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self._carga_horaria = carga_horaria

    @abstractmethod
    def _calcular_bonus(self):
        pass

    @property
    def salario(self):
        return int(self._valor_hora * self._carga_horaria * 4.5 + self._calcular_bonus())

    def __str__(self) -> str:
        return f"{super().__str__()} R${self.salario},00"
