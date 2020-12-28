from random import shuffle
from time import sleep

numeros = list()
aposta = list()
for i in range(1, 60):
    numeros.append(i)
c = int(input('De quantos números será sua aposta?'))
q = int(input(f'Quantas cartelas de {c} números você deseja?'))
print('Os jogos sorteados foram:')
for t in range(1, q+1):
    shuffle(numeros)
    aposta = numeros[:c]
    print(f'O jogo {t} é:', end=' ')
    sleep(1)
    print(sorted(aposta))
print('Boa sorte.')