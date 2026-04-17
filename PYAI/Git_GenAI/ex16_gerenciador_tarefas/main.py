# EX. 16: Gerenciador de Tarefas
# Salva tarefas em arquivo .txt. Adicionar, listar, marcar como concluída e remover.

ARQUIVO = "tarefas.txt"


def carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return [linha.rstrip("\n") for linha in f.readlines()]
    except FileNotFoundError:
        return []


def salvar(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        f.write("\n".join(tarefas))
        if tarefas:
            f.write("\n")


while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

    opcao = input("Opção: ").strip()
    tarefas = carregar()

    if opcao == "1":
        descricao = input("Descrição da tarefa: ").strip()
        tarefas.append(f"[ ] {descricao}")
        salvar(tarefas)
        print("Tarefa adicionada.")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa.")
        else:
            for i, t in enumerate(tarefas, 1):
                print(f"  {i}. {t}")

    elif opcao == "3":
        tarefas = carregar()
        if not tarefas:
            print("Nenhuma tarefa.")
        else:
            for i, t in enumerate(tarefas, 1):
                print(f"  {i}. {t}")
            num = int(input("Número da tarefa concluída: ")) - 1
            if 0 <= num < len(tarefas):
                tarefas[num] = tarefas[num].replace("[ ]", "[x]", 1)
                salvar(tarefas)
                print("Tarefa marcada como concluída.")
            else:
                print("Número inválido.")

    elif opcao == "4":
        if not tarefas:
            print("Nenhuma tarefa.")
        else:
            for i, t in enumerate(tarefas, 1):
                print(f"  {i}. {t}")
            num = int(input("Número da tarefa a remover: ")) - 1
            if 0 <= num < len(tarefas):
                removida = tarefas.pop(num)
                salvar(tarefas)
                print(f"Removida: {removida}")
            else:
                print("Número inválido.")

    elif opcao == "5":
        print("Encerrando.")
        break

    else:
        print("Opção inválida.")
