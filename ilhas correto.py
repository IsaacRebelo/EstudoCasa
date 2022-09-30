if __name__ == '__main__':
    ilhas = ['TER', 'PIC', 'FAI', 'GRA', 'SJR']
    tipos = ['Gasolina', 'Gasoleo']

    vendas = [
        [0, 0, 0, 0, 0],     # 0   Gasolina
        [0, 0, 0, 0, 0]      # 1   Gasoleo
    ]

    totais_ilhas = [0, 0, 0, 0, 0]
    totais_tipo = [0, 0]

    while True:
        try:
            for x in range(len(tipos)):
                for y in range(len(ilhas)):
                    vendas[x][y] = int(input(f'Qual foi o número de vendas na {ilhas[y]} do tipo {tipos[x]}? '))
            print(f'\n{vendas}')

            total = 0
            for x in range(len(tipos)):
                total_tipo = 0
                for y in range(len(ilhas)):
                    total_tipo += vendas[x][y]
                    totais_tipo[x] += vendas[x][y]
                print(f'Total de {tipos[x]} = {total_tipo}')

            for y in range(len(ilhas)):
                total_ilhas = 0
                for x in range(len(tipos)):
                    total += vendas[x][y]
                    total_ilhas += vendas[x][y]
                    totais_ilhas[y] += vendas[x][y]
                print(f'Total na {ilhas[y]} = {total_ilhas}')
            print(f'Total = {total}')

            media_vendas = total / len(vendas)
            print(f'Média = {media_vendas}')

            print('')
            print(f'Totais de ilhas {totais_ilhas}')
            print(f'Totais de tipo {totais_tipo}')

            menor = totais_ilhas[0]
            maior = totais_ilhas[0]
            for x in range(1, len(totais_ilhas)):
                if totais_ilhas[x] > maior:
                    maior = totais_ilhas[x]
                if totais_ilhas[x] < menor:
                    menor = totais_ilhas[x]

            ilhas_menor = []
            ilhas_maior = []
            for x in range(len(totais_ilhas)):
                if totais_ilhas[x] == maior:
                    ilhas_maior.append(totais_ilhas[x])
                if totais_ilhas[x] == menor:
                    ilhas_menor.append(totais_ilhas[x])

            print(f'')


            break

        except ValueError:
            print('Insire um valor válido para vendas.')