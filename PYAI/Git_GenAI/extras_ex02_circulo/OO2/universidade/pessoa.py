class Pessoa:
    def __init__(self, nome=None, cpf=-1):
        self._nome = nome
        if cpf != -1 and self.__validar_cpf(cpf):
            self._cpf = self._normalizar_cpf(cpf)
        else:
            raise ValueError("CPF Inválido")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if self.__validar_cpf(cpf):
            self._cpf = self._normalizar_cpf(cpf)
        else:
            raise ValueError("CPF Inválido")

    @staticmethod
    def _normalizar_cpf(cpf):
        if isinstance(cpf, int):
            if cpf < 0:
                raise ValueError("CPF Inválido")
            texto = f"{cpf:011d}"
        elif isinstance(cpf, str):
            texto = "".join(ch for ch in cpf if ch.isdigit())
        else:
            raise ValueError("CPF Inválido")

        if len(texto) != 11:
            raise ValueError("CPF Inválido")

        return int(texto)

    def __validar_cpf(self, cpf):
        try:
            self._normalizar_cpf(cpf)
        except ValueError:
            return False
        return True

    def __str__(self) -> str:
        cpf = f"{self.cpf:011d}"
        return f"{self.nome} {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    def __repr__(self) -> str:
        return f"Pessoa(nome={self.nome!r}, cpf={self.cpf!r})"

    def __eq__(self, other):
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.cpf == other.cpf

    def __lt__(self, other):
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.cpf < other.cpf

    def __le__(self, other):
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.cpf <= other.cpf

    def __gt__(self, other):
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.cpf > other.cpf

    def __ge__(self, other):
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.cpf >= other.cpf

    def __ne__(self, other):
        resultado = self.__eq__(other)
        if resultado is NotImplemented:
            return NotImplemented
        return not resultado
