if __name__ == '__main__':
    vendas = [
        [10, 20, 30, 40, 50],
        [15, 25, 35, 45, 55]
    ]
    print(vendas)

    for venda in vendas:
        print(venda)
        for v in venda:
            print(v)  # imprime os valores individuais

    x = 0
    y = 3  # define as células das listas ou seja, a posição dos números

    print(f'vendas[x][y]= {vendas[x][y]}')

    for x in range(2):
        for y in range(5):  # vai dizer a posição de cada lista de 0 a 4
            print(f'vendas[{x}] [{y}] = {vendas[x][y]}')
            print(f'xxxx')

    for x in range(len(vendas)):
        for y in range(len(vendas[0])):
            print(f'vendas[{x}] [{y}] = {vendas[x][y]}')

    # total de vendas
    total_vendas = 0
    for x in range(2):
        total_linha = 0
        for y in range(5):  # vai dizer a posição de cada lista de 0 a 4
            total_vendas = total_vendas + vendas[x][y]
            total_linha = total_linha + vendas[x][y]
        print(f'total_linha={total_linha}')
    print(f'total_vendas={total_vendas}')
