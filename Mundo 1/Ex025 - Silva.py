## verificando se a pessoa tem silva no nome
nome = str(input('Digite seu nome completo: \n'))
nome = nome.upper()
nome = list(nome.split())
br = 'SILVA' in nome
print('Verificando se você possui o nome Silva: \n{}'.format(br))