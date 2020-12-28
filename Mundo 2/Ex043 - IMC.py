#calculando o IMC
import math
peso = float(input('Qual seu peso?\n'))
altura = float(input('Qual sua altura?\n'))
imc = peso/pow(altura, 2)
print('Seu imc é de {:.2f}.\nClassificado como:'.format(imc))
if imc<18.5:
    print('Abaixo do peso.')
elif imc>=18.5 and imc<25:
    print('Peso ideal.')
elif imc>=25 and imc<30:
    print('Acima do peso.')
elif imc>=30 and imc<40:
    print('Obeso. Cuidado.')
else:
    print('Obesidade mórbida')



