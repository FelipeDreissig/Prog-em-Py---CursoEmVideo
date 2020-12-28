#### fazendo fatorial
n = int(input('O fatorial de qual número?'))
fatorial = 1
while n!=1:
    fatorial = fatorial*n
    n = n - 1
print('O fatorial de {}! é {}.'.format(n, fatorial))