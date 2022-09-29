"implementa uma table com numeros 5 entre 1 e 50"

import random


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)

if __name__ == '__main__':
    numeros = [0,0,0,0,0]
    estrelas = [0,0]

for x in range(5):
    for x in range(len(numeros)):
        while True:
            onumero = get_random(1,50)
            if onumero not in numeros:
                numeros [x] = onumero
                break
    print(numeros)

    for x in range(len(estrelas)):
        while True:
            umnumero = get_random(1, 12)
            if umnumero not in estrelas:
                estrelas [x] = umnumero
                break
    print(estrelas)