import json
import os

path = os.path.join(os.path.dirname(__file__), "data", "db_carrinho.json")


if not os.path.exists(path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
        
def add_carrinho():
    nome_produto = input("Nome do produto: ")
    tipo_produto = input("Tipo do produto: ")
    valor_produto = float(input("Valor do produto: R$ "))

    novo_produto = {
        "nome": nome_produto,
        "tipo": tipo_produto,
        "valor": valor_produto
    }

    
    with open(path, "r", encoding="utf-8") as file:
        dados = json.load(file)
    

    dados.append(novo_produto)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

    print(f"{nome_produto} adicionado com sucesso ao carrinho!")

def remover_carrinho():
    with open(path, "r", encoding="utf-8") as file:
        dados = json.load(file)

    ler_carrinho()
    remover_produto = input("Digite o nome do produto que deseja remover: ")

    # Flag para saber se encontramos ou não
    encontrada = False

    for produto in dados:
        if produto["nome"].lower() == remover_produto.lower():
            dados.remove(produto)
            encontrada = True
            print(f"{remover_produto} removido com sucesso do carrinho!")
            break

    if not encontrada:
        print("Produto não encontrado. Verifique o nome e tente novamente.")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)
    

def ler_carrinho():
    with open(path, "r", encoding="utf-8") as file:
        dados = json.load(file)
        if dados:
            print("\nItens no carrinho:")
            for x in dados:
                print(f"{x['nome']} -- Tipo: {x['tipo']} -- valor: R${x['valor']:.2f}")
    total = sum(produto['valor'] for produto in dados)
    print(f"\nTotal do carrinho: R${total:.2f}")

def limpar_carrinho():
    with open(path, "w", encoding="utf-8") as file:
        json.dump([], file)
    print("Carrinho limpo com sucesso!")
