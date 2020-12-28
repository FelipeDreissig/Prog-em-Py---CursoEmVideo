#### calculadora de multa
v = float(input('Qual era a velocidade do carro? \n'))
l = float(input('Qual era o limite de velocidade na via? '))
if v>l:
    c = (v-l)*7
    print('Você foi multado. O custo é de {:.2f} reais.'.format(c))
else:
    print('Você está dentro do permitido, parabéns.')