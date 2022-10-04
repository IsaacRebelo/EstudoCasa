

frase = input('insira a sua frase')
exclamação = '!'
interrogacao = '?'
pontofinal = '.'

if len(frase) < 10:
    print(f'A frase tem que ter mais que 10 caracteres')

else:
    print(f'{frase}')

final_frase = frase[len(frase) -1]
if final_frase not in exclamação + interrogacao + pontofinal:
    print(f'a frase tem que acabar com pontuação')
