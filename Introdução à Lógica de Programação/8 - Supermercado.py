print('=' * 40)
print('{:^40}'.format('Supermercado Tabajara'))
print('=' * 40)
info_produto = dict()
produtos = list()

while True:
    numero = len(produtos) + 1
    info_produto['numero'] = numero
    info_produto['nome'] = str(input(f'Produto {numero}: '))
    info_produto['valor'] = float(input('Valor: '))
    info_produto['qtd'] = int(input('Quantidade: '))
    info_produto['total'] = (info_produto['valor'] * info_produto['qtd'])
    produtos.append(info_produto.copy())
    continuar = input('Quer inserir outro produto?S/N ')

    if continuar.lower() != 's':

        print('=' * 40)
        print('{:^40}'.format('Confirmação e Exclusão'))
        print('=' * 40)
        retirar = input('Quer retirar algum produto?S/N ')

        num_produto = int(input("Qual o número do produto? "))
        encontrado = None

        for produto in produtos:
            if produto["numero"] == num_produto:
                encontrado = produto
                produtos.remove(produto)
                print(f"Item {produto['nome']} excluído!")
                break


        if encontrado is None:
            print("Item não encontrado.")
            retirar = input('Quer retirar algum produto?S/N ')


        if retirar.lower() != 's':
            print('=' * 40)
            print('{:^40}'.format('Resumo das Compras'))
            print('=' * 40)

            total = 0
            print("{:<5} {:<15} {:<10} {:<10} {:<10}".format("Nº", "Produto", "Valor", "Qnt", "Total"))
            for produto in produtos:
                total += produto["total"]
                print(
                    "{:<5} {:<10} {:<5.2f} {:<5} {:<5.2f}".format(produto["numero"], produto["nome"], produto["valor"],
                                                                  produto["qtd"], produto["total"]))

            print("\nTotal: {:>25.2f}".format(total))
            break
            