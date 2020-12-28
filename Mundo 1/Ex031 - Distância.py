# calculando o preço da passagem
d = float(input('Qual a distância da viagem?'))
if d>200:
    custo = d*0.2
    print('O preço da passagem é de {:.2f} reais.'.format(custo))
else:
    custol = d*0.45
    print('O preço da passagem é de {:.2f} rais'.format(custol))