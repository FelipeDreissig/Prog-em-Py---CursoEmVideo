## separando

numeros = [[], []]
for c in range(1, 8, 1):
    n = int(input(f'Digite o {c}º número:'))
    if n%2==0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares difitados foram {numeros[0]}')
print(f'Os valores ímpares difitados foram {numeros[1]}')