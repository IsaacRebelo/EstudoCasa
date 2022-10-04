dia = 86400

n1 = int(input(f'Insira um numero '))
n2 = int(input(f'Insira um numero'))
n3 = int(input(f'Insira um numero negativo'))

conta = n1 / 86400
conta2 = n2 /86400
conta3 = n3 /86400

print(f'n1 corresponde a{conta}')
print(f'n2 corresponde a {conta2}')
print(f'n3 corresponde a {conta3}')
while True:
    if n3 > 0:
        print(f' o numero nunca pode ser maior que 0, apresente um numero negativo')

