## primos
n = int(input('Digite um número inteiro:'))
k = 0
for x in range(1, n+1,1):
    if n%x==0:
        k = k + 1
    else:
        k= k + 0

if k==2:
    print('O número {} é um número primo.'.format(n))
else:
    print('O número {} não é um número primo.'.format(n))