#### aumento salarial
sal = float(input('Qual é o seu salário? '))
if sal>1250:
    sal = sal*1.1
    print('O seu novo salário é de {:.2f} reais.'.format(sal))
else:
    sal = sal*1.15
    print('O seu novo salário é de {:.2f} reais.'.format(sal))