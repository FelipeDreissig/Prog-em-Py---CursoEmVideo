n = int(input('Digite um valor: '))
escolha = int(input('Digite: \n- 1 para binário: \n- 2 para octal: \n- 3 para Hexadecimal: \nEscolha sua opção pelo Número: '))
if escolha==1:
    print('O Número {} decimal equivale a {} em binário '.format(n, bin(n).strip('0b')))
elif escolha==2:
    print('O Número {} decimal equivale a {} em Octal'.format(n, oct(n).strip('0o')))
elif escolha==3:
    print('O Número {} decimal equivale a {} em Hexadecimal'.format(n, hex(n).strip('0x')))
else:
    print('Você escolheu uma opção inválida.')