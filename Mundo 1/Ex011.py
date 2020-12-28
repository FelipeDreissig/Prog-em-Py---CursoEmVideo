#calculadora de quantidade de tinta necessária
print('Esta calculadora mostrará a quantidade de tinta necessária, \n'
      'para pintar uma parede.')
altura = float(input('Qual a altura da parede?'))
largura = float(input('Qual a largura da parede?'))

area = largura*altura
quant = area/2
print('A dimensão da parede é {:.2f}X{:.2f} e tem {:.2f} m².'.format(altura, largura, area))
print('levando-se em consideração que um litro de tinta pinta 2m², \n'
      'a quantidade de tinta necessária para a pintura é {:.2f} litros.'.format(quant))