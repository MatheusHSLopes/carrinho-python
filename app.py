from carrinho_compras import add_carrinho, remover_carrinho, ler_carrinho, limpar_carrinho

def apresentação():
    print("=" * 40)
    print("Seja bem-vindo ao Carrinho de Compras Mathz!")
    first_name = input("Digite seu nome: ")
    last_name = input("Agora seu sobrenome: ")
    print(f"Certo {first_name} {last_name}, digite o que você quer fazer:")
    print("=" * 40)

def menu():
    while True:
        escolha = int(input("\nMenu:\n1 para adicionar item ao carrinho\n2 para remover item\n3 ler carrinho\n4 Limpar carrinho \n5 Sair\nEscolha: "))
        if escolha == 1:
            add_carrinho()
        elif escolha == 2:
            remover_carrinho()
        elif escolha == 3:
            ler_carrinho()
        elif escolha == 4:
            limpar_carrinho()
        elif escolha == 5:
            print("Até mais!")
            print("=" * 40)
            break
        
        else:
            print("Opção inválida, tente novamente.")
            print("=" * 40)

apresentação()
menu()
