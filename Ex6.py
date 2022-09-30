

def minandmax():
    num = [1,2,3,4,5,6,7,8]

    min = num[0]
    for a in num:
        if a < min:
            min = a
    print(f' valor minimo é {min}')


    max = num[0]
    for a in num:
        if a > max:
            max = a
    print(f'valor máximo é {max}')


minandmax()




