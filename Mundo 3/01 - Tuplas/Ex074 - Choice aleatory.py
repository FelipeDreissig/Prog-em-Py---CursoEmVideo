# sorteando números aleatórios (metodo 1)
#escolha é uma tupla, segue
from random import randint
escolha = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Sorteei os valores, {escolha}.')
print(f'O maior valor é {max(escolha)}')
print(f'O menor valor é {min(escolha)}')




# sorteando números aleatórios (metodo 2)
escolha = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Sorteei os valores, {escolha}.')
maior = 0
menor = 11
for c in escolha:
    if c<menor:
        menor = c
    if c>maior:
        maior = c
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')