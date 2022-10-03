if __name__ == '__main__':
    ilhas = ['Ter', 'Pic', 'Gra', 'Fai', 'SJR']  # x
    tipos = ['Gasolina', 'Gasoleo']  # y
    vendas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    totais = [0,0,0,0,0]

    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            while True:
                try:
                    vendas[x][y] = (int(input(f'Insira vendas de {tipos[x]} para a ilha {ilhas[y]}')))
                    break
                except ValueError:
                    print(f'Insira um valor válido para vendas de {tipos[x]} na ilha {ilhas[y]}')

    # Imprimir vendas por tipo
    for x in range(len(vendas)):
        total = 0
        for y in range(len(vendas[x])):
            total += vendas[x][y]
        print(f'Total de vendas para {tipos[x]} = {total}')

        # Imprimir vendas por ilha
        z = 0
    for y in range(len(vendas[z])):
        z += 1
        total = 0
        for x in range(len(vendas)):
            total += vendas[x][y]
            print(f'Total de vendas para {ilhas[y]} = {total}')


 # imprimir total de vendas
    total = 0
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            total += vendas[x][y]
        print(f'Total de vendas = {total}')

 # Ilhas com vendas máximas

    maior = totais[0] #define a casa da lista
    menor = totais[0]
    for x in range(1, len(totais)):
     if totais[x] > maior:
         maior= totais[x]
    if totais[x] < menor:
        menor = totais [x]

        maior_ilhas = []
        ilhas_menor = []

    for x in range(len(totais)):
        if totais[x] == maior:
            maior_ilhas.append(ilhas[x])
        if totais[x] == menor:
            ilhas_menor.append(ilhas[x])

    print(totais)
    print(f'ilhas_maior = {maior_ilhas} = {maior}')
    print(f'ilhas_menor = {ilhas_menor} = {menor}')

