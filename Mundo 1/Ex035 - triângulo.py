#### verificando a existência de um triângulo
n1 = float(input('Qual o complimento, em metros, da primeira reta?'))
n2 = float(input('Qual o comprimento, em metros, da segunda reta?'))
n3 = float(input('Qual o comprimento, em metros, da terceira reta?'))

if n1<(n2+n3) and n2<(n1+n3) and n3<(n1+n2):
    print('Com as medidas, {:.2f}, {:.2f} e {:.2f}, é possível formar um triângulo.'.format(n1, n2, n3))
else:
    print('Com as medidas, {:.2f}, {:.2f} e {:.2f}, não é possível formar um triângulo.'.format(n1, n2, n3))