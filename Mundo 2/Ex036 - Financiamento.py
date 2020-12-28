#### verificando a possibilidade de financiar
nome = str(input('Qual o seu nome:\n')).strip().lower()
renda = float(input('Qual a sua renda:\n'))
valor = float(input('Qual o valor da casa(em mil):\n'))
temp = float(input('Em quantos anos você deseja pagá-la:\n'))
rendamax = renda*0.3
valor_mes = valor/(temp*12)
if valor_mes>rendamax:
    print('{}, Levando-se em consideração essas informações, o seu limite de prestação é de {} reais.'
          '\nDessa forma, você não poderá comprar esse imóvel porque o seu custo mensal é de {:.2f} reias'.format(nome.title(), rendamax, valor_mes))
else:
    print('{}, parabéns. Você pode adquirir esse imóvel. o seu limite de pestação é de {} reais.\n'
          'A sua prestação é de {:.2f}'.format(nome.title(), rendamax,valor_mes))