########## quantidade de pessoas
print('-'*20)
print('Conhecendo Pessoas')
print('-'*20)
cont_idade=cont_homem=cont_mulher18=0
idade=0
while True:
    s = sexo = ' '
    idade = int(input('Qual a idade?\n'))
    while sexo not in 'mf':
        sexo = str(input('Qual o sexo? [M/F]\n')).strip().lower()[0]
    if idade<18:
        cont_idade = cont_idade + 1
    if sexo =='m':
        cont_homem = cont_homem + 1
    if sexo =='f' and idade<18:
        cont_mulher18 = cont_mulher18 + 1
    while s not in 'sn':
        s = str(input('Deseja continuar? [S/N]\n')).strip().lower()[0]
    if s == 'n':
        break
print(f'A quantidade de pessoas com 18 anos é {cont_idade}.')
print(f'A quantidade de homens é {cont_homem}.')
print(f'A quantidade de mulheres com menos de 18 anos é {cont_mulher18}.')


