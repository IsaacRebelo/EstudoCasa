

while True:
    numero_um= int(input('Insira o primeiro numero'))
    numero_dois= int(input('Insira o segundo numero'))
    soma = numero_um + numero_dois
    if numero_dois < numero_um:
        print(f'O n1 nunca pode ser maior que o n2')

    else:
        print(f'{soma}')

