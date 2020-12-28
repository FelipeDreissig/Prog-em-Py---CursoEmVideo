## listtinha boba
cond = 's'
c = 1
quant = 0
l = []
while cond=='s':
    if c == 1:
        n_aux = int(input(f'Digite o 1º número:'))
        l.append(n_aux)
    else:
        n = int(input(f'Digite o {c}º valor:'))
        l.append(n)
    c = c + 1
    quant = quant + 1
    cond = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
print(f'Foram digitados {quant} número(s).')
j = 0
for c in range(0, len(l)):
    if 5 == l[c]:
        j = j + 1
        print(f'O valor cinco aparece {j} vezes, na posição', end=' ')
        print(f'{c+1}')
if j == 0:
    print('O valor cinco não aparece.')
l.sort(reverse=True)
print(f'Os valores são: {l}')


