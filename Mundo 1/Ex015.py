## aluguel de carros

km = float(input('Quantos kilometros foram rodados com o carro alugado: Km \n'))
d = int(input('Quantos dias foram alugados: '))

p = 60*d + 0.15*km

print('O preço a pagar é de {:.2f} reais.'.format(p))
