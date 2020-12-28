### verificando o alistamento
from datetime import date
nome = str(input('Qual o teu nome:\n')).strip().title()
nas = int(input('Qual o ano de seu nascimento:\n'))
hoje = int(date.today().year)
idade = hoje - nas
if idade==18:
    print('{}, você precisa se alistar.'.format(nome))
elif idade>18:
    print('{}, já passou seu prazo.Ele venceu há {} anos'.format(nome, idade-18))
elif idade<18:
    print('{}, não fique ansioso, sua vez chegará.\n Faltam {} para você se alistar'.format(nome, 18-idade))
