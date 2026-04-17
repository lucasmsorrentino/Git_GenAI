# EX. 13: Agenda Telefônica
# Adicionar, buscar, listar e remover contatos.

agenda = {}

while True:
    print("\n--- Agenda Telefônica ---")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Listar contatos")
    print("4. Remover contato")
    print("5. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        agenda[nome] = telefone
        print(f"Contato '{nome}' adicionado.")

    elif opcao == "2":
        nome = input("Nome a buscar: ").strip()
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        if not agenda:
            print("Agenda vazia.")
        else:
            print("Contatos:")
            for nome, tel in sorted(agenda.items()):
                print(f"  {nome}: {tel}")

    elif opcao == "4":
        nome = input("Nome a remover: ").strip()
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' removido.")
        else:
            print("Contato não encontrado.")

    elif opcao == "5":
        print("Encerrando.")
        break

    else:
        print("Opção inválida.")
