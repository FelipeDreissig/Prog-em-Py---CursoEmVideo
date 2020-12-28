# fazendo uma PA
print('Vamos fazer uma progressão aritmética')
i = int(input('Qual o início:'))
f = int(input('Qual o fim: '))
r = int(input('Qual a razão: '))
if i<f and r>0:
    while i<f:
        print(i, '-', end=' ')
        i = i + r
elif i<f and r<0:
    r = (-1)*r
    print('O sinal da razão está errado. Não se preocupe, Já corrigi para o inverso.')
    while i<f:
        print(i, '-', end=' ')
        i = i + r
elif i>f and r>0:
    r = r*(-1)
    print('O sinal da razão está errado. Não se preocupe, Já corrigi para o inverso.')
    while f<i:
        print(i, '-', end=' ')
        i = i + r
elif i>f and r<0:
    while f<i:
        print(i, '-', end=' ')
        i = i + r
print('Fim')


