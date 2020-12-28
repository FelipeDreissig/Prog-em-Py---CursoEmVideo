#### calculando tudo
mais_idade = 0
t_idade = 0
k = 0
nome_maisvelho = ''
for x in range(1,5,1):
    print("===== {}ª pessoa =====".format(x))
    nome = str(input('Qual o seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('VOcê é do sexo masculino ou fenino?[M/F] ')).strip().lower()
    t_idade = idade + t_idade
    if sexo=='m' and idade>mais_idade:
        mais_idade = idade
        nome_maisvelho = str(nome.strip().title())
    if sexo=='f' and idade<20:
        k = k + 1
media = float(t_idade/4)
print('A idade média é de {:.2f}\nO nome do homem mais velho é {} e sua idade é de {} anos.\nA quantidade pessoas com menos de 20 anos e do sexo feminino é de {}'.format(media, nome_maisvelho, mais_idade, k))
