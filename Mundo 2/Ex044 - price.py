#### formas de pagamento

price = float(input('Qual o preço das comprar: R$ '))
print("""FORMAS DE PAGAMENTO
[1] À vista (dinheiro ou cheque)
[2] À vista cartão (1x)
[3] 2x no cartão
[4] 3x ou mais no cartão
""")
met = int(input('Qual a forma de pagamento: \n'))
if met==1:
    price = price*0.9
    print('O valor total a ser pago é de {} reais.'.format(price))
elif met==2:
    price = price*0.95
    print('O valor total a ser pago é de {} reais.'.format(price))
elif met==3:
    price = price/2
    priceaux = price
    print('Parcelado em 2x e o valor de cada parcela é de {} reais.\nTotalizando {} reais.\n Não há incidência de juros.'.format(price, priceaux))
elif met==4:
    v = int(input('Quantas vezes você deseja parcelar?'))
    price2 = (price*1.2)/v
    priceaux = price*1.2
    print('O valor é {}x de  {} reias.\nTotalizando {} reais.'.format(v, price2, priceaux))

