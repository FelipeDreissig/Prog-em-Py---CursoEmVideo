# arredondando números
import math
n = float(input('Digite um número qualquer: '))
intei = math.trunc(n) #trunc traz o número inteiro
print('O número {} tem a parte inteira {}.'.format(n, intei))

## ou, de outra forma, onde estiver intei, fazemos o seguinte:
intei2 = int(math.fabs(n))

