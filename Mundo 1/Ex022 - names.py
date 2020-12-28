### criando um programa de string básico

nome = str(input('Escreva seu nome completo: \n'))

nome_maiusculo = nome.upper()
print('O nome em maúsculo é \n{}'.format(nome_maiusculo))

nome_minusculo = nome.lower()
print('O nome em minúsculas é \n{}'.format(nome_minusculo))

nome_title = nome.title()
print('O nome com as primeiras letras em maiúsculo é \nF{}'.format(nome_title))

nome_captalize = nome.capitalize()
print('O nome com a primeira letra do primeiro nome em maiúsculo é \n{}'.format(nome_captalize))

nome_tamanho = list(nome.split(sep=' '))
nome_tamanho = len(''.join(nome_tamanho))
print('O tamanho do nome completo é de {} casas.'.format(nome_tamanho))

nome_primeiro = nome.split(sep=' ')
nome_primeiro = nome_primeiro[0]
nome_primeiro_t = int(len(nome_primeiro))
print('O primeiro nome é \n {}'.format(nome_primeiro))
print('O tamanho do primeiro nome é de {} casas.'.format(nome_primeiro_t))


nome_segundo = nome.split(sep=' ')
nome_segundo = nome_segundo[1]
nome_segundo_t = int(len(nome_segundo))
print('O segundo nome é \n {}'.format(nome_segundo))
print('O tamanho do segundo nome é de {} casas.'.format(nome_segundo_t))

nome_terceiro = nome.split(sep=' ')
nome_terceiro = nome_terceiro[2]
nome_terceiro_t = int(len(nome_terceiro))
print('O terceiro nome é \n {}'.format(nome_terceiro))
print('O tamanho do terceiro nome é de {} casas'.format(nome_terceiro_t))


