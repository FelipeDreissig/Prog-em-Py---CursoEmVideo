from random import randint

def sorteia(l):
    for k in range(0, 5):
        l.append(randint(1, 10))


def somapar(j):
    soma = 0
    for p in range(0, len(j)):
        if j[p]%2 == 0:
            soma = soma + j[p]
    return soma


print('Soteando valores.')
numeros = list()
sorteia(numeros)
print(numeros)
print(f'A soma dos valores pares é {somapar(numeros)}.', end=' ')

