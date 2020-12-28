seg = 'S'
c = q = menor = maior = media = 0
while seg =='S':
    n = int(input('Digite um número?\n'))
    q = q + n
    c = c + 1
    if c == 1:
        maior = menor = n
    else:
        if n>maior:
            maior = n
        elif n<menor:
            menor = n
    seg = str(input('Deseja continuar? [S/N]\n')).strip().upper()[0]
media = q/c
print('A média é de {:.2f}.\nA soma dos números é de {}.\nO menor e o maior são, respectivamente, {} e {}.'.format(media, q, menor, maior))
