empregado = input(f'Insira o seu nome')
salario_hora = float(input('quanto recebe à hora ?'))
numero_de_horas = float(input('quantas horas trabalhou esta semana'))

pagamento = salario_hora * numero_de_horas


if numero_de_horas > 40:
    diferenca = numero_de_horas - 40
    pagamento = 40 * salario_hora # o que ia receber numa semana normal
    extra = diferenca * (salario_hora * 2)
    pagamento= pagamento + extra
print(f'{pagamento}')











