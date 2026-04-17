# Desafio 1: Validador de CPF
# Implementa a validação oficial do CPF brasileiro.


def validar_cpf(cpf: str) -> bool:
    # Remove formatação
    cpf = "".join(c for c in cpf if c.isdigit())

    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    # Primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False

    # Segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    return digito2 == int(cpf[10])


cpf = input("Digite o CPF (com ou sem formatação): ").strip()

if validar_cpf(cpf):
    print("CPF VÁLIDO.")
else:
    print("CPF INVÁLIDO.")
