#### jo KEN PO
import random
from time import sleep
aceite = int(input('Olá, eu sou seu computador. Gostaria de jogar jokenpô?\n1 - Sim\n2 - Não\n'))
escolhapc = random.choice([1, 2, 3])
if aceite == 1:
    escolhahumano = int(input("""Escolha uma das opções:
1 - Pedra
2 - Papel
3 - Tesoura    
    \n"""))
    if escolhahumano == 1 or escolhahumano == 2 or escolhahumano == 3:
        print('JO')
        sleep(1)
        print('ken')
        sleep(1)
        print('PO')
        sleep(1)
        if escolhapc == escolhahumano:
            print('Vocês empataram')
        elif escolhapc == 1:
            if escolhahumano == 2:
                print('O humano venceu. o PC escolheu {} e o humano escolheu {}.'.format('pedra', 'papel'))
            elif escolhahumano == 3:
                print('O PC venceu. O pc escolheu {} e o humano escolheu {}.'.format('pedra','tesoura'))
        elif    escolhapc == 2:
            if escolhahumano == 1:
                print('O PC venceu. O PC escolheu {} e o humano escolheu {}.'.format('papel', 'pedra'))
            elif escolhahumano == 3:
                print('O humano venceu. O PC escolheu {} e o humano escolheu {}'.format('papel', 'tesoura'))
        elif escolhapc == 3:
            if escolhahumano == 1:
                print('O homem venceu. O PC escolheu {} e o homem escolheu {}.'.format('tesoura', 'pedra'))
            elif escolhahumano == 2:
                print('O PC venceu. O pc escolheu {} e o homem escolheu {}.'.format('tesoura', 'papel'))
    else:
        print('\33[30;41mOpção inválida, tente novamente.\33[m')
elif aceite == 2:
    print('Fica para a próxima.')
else:
    print('\33[30;41mOpção inválida, tente novamente.\33[m')