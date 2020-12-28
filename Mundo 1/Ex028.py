##### esolhendo o npumero certo
import random
from time import sleep
print('Brincadeira da adivinhação.')
lista = [0, 1, 2, 3, 4, 5]
num = int(input('Escolha um número de 0 a 5:\n'))
escolhapc = random.choice(lista)
print('Pensando')
sleep(3)
if num == escolhapc:
    print('Parabéns, você acertou.')
else:
    print('Você errou, infelizmente. \nO número escolhido foi {}.'.format(escolhapc))

