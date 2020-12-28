from time import sleep
c = ''
li = (1, 2, 3, 4, 5, 6)
while c != 6:
    n1 = float(input('Digite o primeiro número:\n'))
    n2 = float(input('Digite o segundo número:\n'))
    print('Escolha uma das opções:\n')
    o = int(input('[1] - Somar\n'
          '[2] - subtrair\n'
          '[3] - multiplicar\n'
          '[4] - Maior\n'
          '[5] - Novos números\n'
          '[6] - Encerrar\n'))
    if o == 1:
        soma = n1+n2
        print('A soma é {}.'.format(soma))
    elif o == 2:
        su = int(input('Operação desejada\n'
                       '[1] - Subtrair {0} do {1}.\n'
                       '[2] - Subtrair {1} do {0}.\n'.format(n2, n1)))
        if su == 1:
            resu = n1 - n2
            print('O resultado é {}.\n'.format(resu))
        elif su == 2:
            resu2 = n2 - n1
            print('O resultado é {}.\n'.format(resu2))
    elif o == 3:
        mult = n1*n2
        print('O resuldado da multiplicação é {}.\n'.format(mult))
    elif o == 4:
        if n1>n2:
            print('O maior é {}.\n'.format(n1))
        elif n2>n1:
            print('O maior é {}.\n'.format(n2))
        elif n1==n2:
            print('São iguais.')
    elif o == 6:
        print('Prrograma sendo encerrado.')
        sleep(1)
        c = 6
        print('Até a próxima.')
    elif o == 5:
       print('Reiniciando.')
    else:
        print('\033[7;31;40mOpção inválida, tente novamente.\033[m\n')