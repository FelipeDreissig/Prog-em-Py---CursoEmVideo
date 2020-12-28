# maior número
n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))
if (n1>n2) and (n1>n3):
    if n2>n3:
        print('O maior número é {}.\nO o menor é {}.'.format(n1, n3))
    else:
        print('O maior número é {}.\nO menor número é {}.'.format(n1, n2))
if (n2>n1) and (n2>n3):
    if n1>n3:
        print('O maior número é {}.\nO menor número é {}.'.format(n2, n3))
    else:
        print('O maior número é {}.\nO menor número é {}'.format(n2, n1))
if (n3>n1) and (n3>n2):
    if n1>n2:
        print('O maior número é {}.\n O menor número é {}.'.format(n3, n2))
    else:
        print('O maior número é {}.\nO menor número é {}.'.format(n3, n1))