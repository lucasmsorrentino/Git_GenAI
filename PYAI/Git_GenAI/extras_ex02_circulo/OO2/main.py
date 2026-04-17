from universidade.disciplina import Disciplina
from universidade.pessoa import Pessoa
from universidade.professor_adjunto import ProfessorAdjunto
from universidade.professor_substituto import ProfessorSubstituto


def demonstrar_pessoas():
    lista = [
        Pessoa("João da Silva", 77777777777),
        Pessoa("Maria", 11111111111),
        Pessoa("Pedro", 55555555555),
        Pessoa("Camila", 88888888888),
    ]
    lista.sort()
    for pessoa in lista:
        print(pessoa)


def demonstrar_professores():
    professor_adjunto = ProfessorAdjunto("Maria", 22222222222)
    professor_adjunto.qtde_proj_pesquisa = 3

    professor_substituto = ProfessorSubstituto("João", 11111111111)
    professor_substituto.anos_trabalho = 2

    disciplina1 = Disciplina("Orientação a Objetos", 60, professor_adjunto)
    disciplina2 = Disciplina("Algoritmos", 60, professor_substituto)

    print(disciplina1.nome)
    print(disciplina1.professor.nome)
    print(disciplina1.professor._calcular_bonus())
    print(disciplina2.nome)
    print(disciplina2.professor.nome)
    print(disciplina2.professor._calcular_bonus())
    print(professor_adjunto)
    print(professor_substituto)


def demonstrar_validacao():
    try:
        pessoa = Pessoa("Maria", 11111111111)
        pessoa.cpf = 123
        print(pessoa.nome)
        print(pessoa.cpf)
    except ValueError as exc:
        print("O CPF não é válido!")
        print(exc)


def main():
    demonstrar_pessoas()
    demonstrar_professores()
    demonstrar_validacao()


if __name__ == "__main__":
    main()
