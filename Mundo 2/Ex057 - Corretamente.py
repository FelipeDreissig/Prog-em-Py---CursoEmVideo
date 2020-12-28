### leitura correta
sexo = str(input('Qual o seu sexo?[M/F]\n')).strip().lower()
while sexo!='f' and sexo!='m':
    sexo = str(input('Qual o seu sexo?[M/F]\n'))
print('Está correto!')

