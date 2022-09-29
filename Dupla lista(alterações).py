if __name__ == '__main__':
    vendas = [
        [10, 20, 30, 40, 50],
        [15, 25, 35, 45, 55]
    ]
    print(vendas)

    x = 0
    y = 0
    print(f'vendas[x][y]= {vendas[x][y]}')


    for y in range(5):
        for x in range (2):
            print(f'vendas[{x}] [{y}] = {vendas[x][y]}')

    total_vendas = 0
    for y in range(5):
        total_linha = 0
        for y in range(2):  # vai dizer a posição de cada lista de 0 a 4
            total_vendas = total_vendas + vendas[x][y]
            total_linha = total_linha + vendas[x][y]
        print(f'total_linha={total_linha}')
        print(f'total_vendas={total_vendas}')

