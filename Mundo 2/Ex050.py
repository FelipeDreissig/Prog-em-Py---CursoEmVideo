## soma de valores
l = 0
k = 0
for c in range(1,7):
    num = int(input('Digite um valor: '))
    if  num%2==0:
        k = num + k
        l = l + 1
print('A soma dos números pares é {}. E a quantidade de números pares é {}.'.format(k, l))