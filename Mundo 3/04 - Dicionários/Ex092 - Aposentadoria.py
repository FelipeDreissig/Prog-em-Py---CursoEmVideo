from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Digite seu nome:')).strip().lower().capitalize()
nascimento = int(input('Digite sua data de nascimento:(em anos) '))
idade = datetime.now().year - nascimento
cadastro['idade'] = idade
print('Caso não possua carteira de trabalho, digite 0 (zero).', end= ' ')
cadastro['carteira'] = int(input('Digite o nº da sua carteira de trabalho, apenas os 4 primeiros dígitos:\n'))
if cadastro['carteira'] == 0:
    print('Você precisa possuir carteira de trabalho para se aposentar.\n Até a próxima.')
else:

    cadastro['ano de contratação'] = int(input('Qual foi o ano de contratação:'))
    cadastro['salario'] = float(input('Digite seu salário:'))
    faltaaposentar = 35 - (datetime.now().year - cadastro['ano de contratação'])
print(f'{cadastro["nome"]}, faltam {faltaaposentar} anos para você se aposentar. '
      f'Você irá aposentar com {faltaaposentar+idade} anos de idade.')
