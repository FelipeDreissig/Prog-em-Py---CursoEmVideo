
lista = []
while True:
    c = ' '
    n = int(input('Digite um valor:'))
    if n in lista:
        print('Este não vale. ELe já está.')
    else:
        lista.append(n)
        print(f'O valor {n} foi adicionado com sucesso.')
    while c not in 'sn':
        c = str(input('Voce deseja continuar? [S/N]')).strip().lower()[0]
    if c == 'n':
        break
print(f'Os valores digitados foram, {sorted(lista)}')


