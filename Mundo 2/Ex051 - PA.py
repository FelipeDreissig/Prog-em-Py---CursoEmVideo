# fazendo uma PA
print('Vamos fazer uma progressão aritmética')
i = int(input('Qual o início:'))
f = int(input('Qual o fim: '))
r = int(input('Qual a razão: '))
if i<f and r>0:
    for x in range(i,f,r):
        print(x, '-', end=' ')
elif i<f and r<0:
    r = (-1)*r
    print('O sinal da razão está errado. Não se preocupe, Já corrigi para o inverso.')
    for x in range(i,f,r):
        print(x, '-', end=' ')
elif i>f and r>0:
    r = r*(-1)
    print('O sinal da razão está errado. Não se preocupe, Já corrigi para o inverso.')
    for x in range(i,f,r):
        print(x, '-', end=' ')
elif i>f and r<0:
    for x in range(i,f,r):
        print(x, '-', end=' ')
print('Fim')


