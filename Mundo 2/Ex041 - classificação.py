############# classificação de idade
idade = int(input('Qual a sua idade:\n'))
if idade<=9:
    print('Mirim')
elif idade>9 and idade<=14:
    print('Infantil')
elif idade>14 and idade<=19:
    print('Júnior')
elif idade>19 and idade<=20:
    print('Sênior')
else:
    print('Master')