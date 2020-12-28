
l = []
par = []
impar = []
c = 's'
k = 1
while c =='s':
    n = int(input(f'Digite o {k}º número:'))
    l.append(n)
    k = k + 1
    c = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
for p in range(0, len(l)):
    if l[p]%2==0:
        par.append(l[p])
    else:
        impar.append(l[p])
par.sort()
impar.sort()
l.sort()
print(f'Os números digitados foram, {l}')
print(f'Os números pares digitados foram, {par}')
print(f'Os números ímpares digitados foram, {impar}')
