# fazendo novamente
l = []
p = 0
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}º valor inteiro:'))
    if len(l)==0:
        l.append(n)
        print(f'{n} adicionado na lista.')
    elif n>l[-1]:
        l.append(n)
        print(f'Adicionado {n} no final da lista.')
    else:
        for k in range(0, 5):
            if n <= l[k]:
                l.insert(k, n)
                print(f'Adicionado {n}, na {k+1}ª posição.')
                break
print(f' Os números são {l}')