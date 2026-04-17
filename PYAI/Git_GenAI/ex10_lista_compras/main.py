# EX. 10: Lista de Compras
# Adicionar itens, remover itens, mostrar lista e encerrar.

lista = []

while True:
    print("\n--- Lista de Compras ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        item = input("Nome do item: ").strip()
        lista.append(item)
        print(f'"{item}" adicionado.')

    elif opcao == "2":
        if not lista:
            print("A lista está vazia.")
        else:
            item = input("Nome do item a remover: ").strip()
            if item in lista:
                lista.remove(item)
                print(f'"{item}" removido.')
            else:
                print("Item não encontrado.")

    elif opcao == "3":
        if not lista:
            print("A lista está vazia.")
        else:
            print("Itens na lista:")
            for i, item in enumerate(lista, 1):
                print(f"  {i}. {item}")

    elif opcao == "4":
        print("Encerrando.")
        break

    else:
        print("Opção inválida.")
