## maior e menor peso
maior = 0
menor = 1000
for x in range(1, 7, 1):
    peso = int(input('Qual o seu peso?'))
    if peso>maior:
        maior = peso
    if peso<menor:
        menor = peso
print('O menor peso foi de {} e o maior peso foi de {}.'.format(menor, maior))