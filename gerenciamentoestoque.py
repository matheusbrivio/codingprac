#Crie um sistema de gerenciamento de estoque para uma loja. O sistema deve permitir adicionar produtos ao estoque, remover produtos, atualizar a quantidade de um produto e visualizar todos os produtos disponíveis. Cada produto deve ser representado por uma lista contendo nome, preço e quantidade.

#Requisitos:
#Escrever uma função adicionar_produto(estoque) que adicione um novo produto ao estoque.
#Escrever uma função remover_produto(estoque, nome) que remova um produto do estoque.
#Escrever uma função atualizar_quantidade(estoque, nome) que atualize a quantidade de um produto existente.
#Escrever uma função visualizar_estoque(estoque) que exiba todos os produtos disponíveis no estoque.
#Dica: para armazenar os valores, utilize uma lista dentro de outra. E armazena os valores da segunda lista por índices fixados, como por exemplo: 0 > Nome, 1 > Preço, 2 > Quantidade.


def adicionar_produto(lista):
    nome = input("Digite o nome do produto:")
    valorproduto = float(input("Digite o valor do produto:"))
    qtdprodudo = int(input("Digite a quantidade do produto a ser adicionado:"))
    produto = [nome, valorproduto, qtdprodudo]
    lista.append(produto)
    print("Produto", nome, "adicionado com sucesso!")

def remover_produto(lista):
    print(lista)
    nome = input("Digite o nome do produto que deseja remover:")
    for i in range (len(lista)):
        if nome == lista[i][0]:
            lista.remove(lista[i])
            print("Produto removido com sucesso!")
            return
    print("O produto não foi encontrado!")

def atualizar_quantidade(lista):
    print(lista)
    nome = input("Digite o nome do produto que deseja editar a quantidade:")
    for i in range (len(lista)):
        if nome == lista[i][0]:
            while True:
                try:
                    quantidade_nova = int(input("Digite a quantidade nova:"))
                    break
                except ValueError:
                    print("Tente uma quantidade válida!")
            lista[i][2] = quantidade_nova
            print("Quantidade atualizada com sucesso!")
            return
    print("O produto", nome, "não foi encontrado!")

def visualizar_estoque(lista):
    print("----Estoque de produtos----")
    print("NOME, VALOR, QUANTIDADE")
    if len(lista) > 0:
        for i in range(len(lista)):
            print("Produto", i + 1,":", lista[i])
        return
    print("O estoque está vazio!")

def main ():
    estoque = []
    opcao = 0
    while opcao != 5:
        print("=== Menu de Opções ===")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Atualizar quantidade")
        print("4 - Visualizar estoque")
        print("5 - Sair")
        while True:
            try:
                opcao = int(input("Digite a opção desejada:"))
                break
            except ValueError:
                print("Tente uma opção válida!")
        if opcao == 1:
            adicionar_produto(estoque)
        elif opcao == 2:
            remover_produto(estoque)
        elif opcao == 3:
            atualizar_quantidade(estoque)
        elif opcao == 4:
            visualizar_estoque(estoque)
        elif opcao == 5:
            print("Voce saiu...")
        else:
            print("Opcão invalida!")
main()
