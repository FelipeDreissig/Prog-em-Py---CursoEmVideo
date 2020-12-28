# Calculadora de desconto
preco = float(input('Qual o preço do produto?\n'))

novo_preco = preco*0.95

print('Levando-se em consideração 5% de desconto\n'
      'o novo preõ será de {:.2f} reais.'.format(novo_preco))