import random

chances = 10
numero_true = random.randint (1, 50)


def naosei ():
    global chances
    while (chances > 0):
        vari = input('tente acertar um numero entre 1 a 50: ')
        try:
            vari = int (vari)
            if vari == numero_true:
                print (f'Voce acertou! o numero era {numero_true} ainda sobrou {chances}')
                break
            else:
                chances -= 1
                if chances > 0:
                    print(f"errado, voce ainda tem {chances} tentativas!")
                else:
                    print (f'voce perdeu todas suas tentativas. o numero correto era {numero_true}')
        except ValueError:
                print ('nao e valido')

naosei()
