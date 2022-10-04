def impar(numero):
    numero = int(numero)
    if numero % 2 != 0:
        return numero
    else:
        return ''
if __name__ == '__main__':


    while True:
        try:
            numero = int(input(f'Insira um numero inteiro positivo: '))
            numero = str(numero)
            impares = ''

            for x in numero:
                impares += str(impar(x))
            print(f'Impares: {impares}')

            continuar = input('Repetir (s | n)')
            if continuar == 'n':
                break

        except ValueError:
            print('Insira Valor valido')

    print(f'Adeus')
