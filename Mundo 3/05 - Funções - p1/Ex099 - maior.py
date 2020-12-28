def maior(k):
    m = 0
    for i in range(0, len(k)):
        if k[i] > m:
            m = k[i]
    print(m)


def menor(j):
    men = j[0]
    for l in range(0, len(j)):
        if j[l] < men:
            men = j[l]
    print(men)

# programa
lista = list()
cri = 's'
while True:
    n = 0
    n = int(input('Digite um número qualquer:'))
    lista.append(n)
    cri = str(input('Deseje continuar?[S/N]')).strip().lower()[0]
    while cri not in 'sn':
        print('Resposta inválida, tente novamente.')
        cri = str(input('Deseje continuar?[S/N]')).strip().lower()[0]
    if cri == 'n':
        break

print(f'O maior valor foi', end=' ')
maior(lista)
print(f'O menor valor foi', end=' ')
menor(lista)

