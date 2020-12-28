#### verificando a existência de um triângulo
n1 = float(input('Qual o complimento, em metros, da primeira reta?\n'))
n2 = float(input('Qual o comprimento, em metros, da segunda reta?\n'))
n3 = float(input('Qual o comprimento, em metros, da terceira reta?\n'))

if n1<(n2+n3) and n2<(n1+n3) and n3<(n1+n2):
    print('Com as medidas, {:.2f}, {:.2f} e {:.2f}, é possível formar um triângulo.'.format(n1, n2, n3))
    if n1==n2==n3:
        print('É um triângulo equilátero')
    elif n1==n2 or n1==n3 or n2==n3:
        print('É um triângulo isóceles')
    else:
        print('É um escaleno. ')
else:
    print('Com as medidas, {:.2f}, {:.2f} e {:.2f}, não é possível formar um triângulo.'.format(n1, n2, n3))