produtos = {}

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ").lower()
        if nome in produtos:
            print("Produto já cadastrado!")
        else:
            produtos[nome] = {"preco": input("Preço do produto: "), "quantidade": input("Quantidade do produto: ")}
            print(f"Produto {nome} cadastrado com sucesso!")

    if opcao == "2":
        print("LISTA DE PRODUTOS")
        if produtos:
            for nome in produtos:
                preco = produtos[nome]["preco"]
                quantidade = produtos[nome]["quantidade"]
                print(f"Nome: {nome}, Preço: {preco}, Quantidade: {quantidade}")
        else:
            print("Produto não encontrado")

    if opcao == "3":
        nome = input("Nome do produto para atualizar: ").lower()
        if nome in produtos:
            print("1 - Atualizar preço")
            print("2 - Atualizar quantidade")
            escolha = input("Escolha o que deseja atualizar: ")

            if escolha == "1":
                novo_preco = input("Novo preço: ")
                produtos[nome]["preco"] = novo_preco
                print("Preço atualizado!")

            if escolha == "2":
                nova_quantidade = input("Nova quantidade: ")
                produtos[nome]["quantidade"] = nova_quantidade
                print("Quantidade atualizada!")
        else:
            print("Produto não encontrado.")

    if opcao == "4":
        nome = input("Nome do produto para deletar: ").lower()
        if nome in produtos:
            del produtos[nome]
            print("Produto deletado!")
        else:
            print("Produto não encontrado.")

    if opcao == "5":
        print("Saindo do programa.")
        break

    if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        print("Opção inválida.")
