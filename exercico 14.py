numero = input('insira um numero')
digito = str(numero)
numero_split = numero.split()
print(f'{numero_split}')
valor = 0
for x in range(0,len(digito)):
    valor += int(digito[x])
    print(f'{valor}' )

