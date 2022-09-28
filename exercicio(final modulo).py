





if __name__ == '__main__':


        while True:
            frase = (input('Insira uma frase'))
            final_da_frase = frase[len(frase)-1]
            x = 0
            for c in frase:
                x +=1
            print(f' A frase tem {x} caracteres')

            if len(frase) <10:
                print(f'nao da')
                continue

            if len(frase) >10:
                print(f'da')
                break

            if final_da_frase not in "!" + "?" + ".":
                print(f'A tua frase tem que acabar com alguma coisa')
                break
















