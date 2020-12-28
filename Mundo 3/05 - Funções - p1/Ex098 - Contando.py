from time import  sleep
def contador(i, f, r):
    if i < f:
        if r > 0:
            for k in range(i, f+1, r):
                sleep(0.25)
                print(k, end=' ')
        else:
            for k in range(i, f+1, -r):
                sleep(0.25)
                print(k, end=' ')
    if f < i:
        if r > 0:
            for k in range(i, f-1, -r):
                sleep(0.25)
                print(k, end=' ')
        else:
            for k in range(i, f-1, r):
                sleep(0.25)
                print(k, end=' ')


print('\033[7;31;40mContado de 1 até 10 com razao 1.\033[m')
contador(1, 10, 1)
print('\nFim.')
print('\033[7;33;40mContando de 2 até 0 com razão 2.\033[m')
contador(10, 0, 2)
print('\nFim.')
print('\033[7;34;40mContagem personalizada.\033[m')
ini = int(input('Digite o início:'))
fim = int(input('Digite o fim:'))
raza = int(input('Qual a razão:'))
if raza == 0:
    print('Você quer uma razão inválida, dessa forma, a razão será o valor 1.')
    raza = 1
contador(ini, fim, raza)
print('\nFim.')
