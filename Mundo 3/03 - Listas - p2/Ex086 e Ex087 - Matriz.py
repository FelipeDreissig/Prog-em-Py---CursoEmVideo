# criando uma matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {[l+1], [c+1]}:'))
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c]%2 == 0:
            pares = pares + matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
    coluna3 = coluna3 + matriz[l][2]
for t in range(0, len(matriz)):
    print(matriz[t])
print(f'A soma dos valores pares é: {pares}.')
print(f'A soma dos valores da 3ª coluna é: {coluna3}.')
print(f'O maior número da segunda linha é: {maior}.')

