##### esolhendo o npumero certo
import random
from time import sleep
num = 'a'
escolhapc = 'b'
c = 0
while num != escolhapc:
    print('Brincadeira da adivinhação.')
    lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    num = int(input('Escolha um número de 0 a 10:\n'))
    print('Pensando')
    sleep(1)
    escolhapc = random.choice(lista)
    if num == escolhapc:
        print('\033[30;42mParabéns, você acertou.\033[m\n')
    else:
        print('\033[7;31;40mVocê errou, infelizmente.\033[m\n\033[7;31;40mO número escolhido foi {}.\033[m\n'.format(escolhapc))
    c = c + 1
print('Foram necessárias {} vezes até você acertar.\n'.format(c))
