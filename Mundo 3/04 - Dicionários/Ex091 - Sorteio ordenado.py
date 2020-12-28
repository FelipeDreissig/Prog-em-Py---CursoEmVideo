from random import randint
from operator import itemgetter
n = int(input('Quantas pessoas vão jogar?\n'))
jogadores = dict()
listagem = list()
for i in range(1, n+1):
    jogadores[f'jogador {i}'] = randint(1, 6)
listagem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, c in enumerate(listagem):
    print(f'{i+1}ª   {c[0]}      {c[1]}')

