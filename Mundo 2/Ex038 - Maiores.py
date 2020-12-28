## verificando o maior número
n1 = float(input('Digite o primeiro número\n'))
n2 = float(input('Digite o segundo número:\n'))

if n1>n2:
    d = n1-n2
    print('O primeiro número é o maior, sendo sua diferença de {:.2f}.'.format(d))
elif n2>n1:
    d = n2-n1
    print('O segundo número é o maior, sendo sua difereça de {:.2f}.'.format(d))
else:
    print('Os dois números são iguais.')