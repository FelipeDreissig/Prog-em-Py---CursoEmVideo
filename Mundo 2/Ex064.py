n = 0
soma = 0
quant = 0
while n!=999:
    n = int(input('Digite algum número inteiro:\nSe quiser encerrar, basta digitar 999.\n'))
    if n!=999:
        soma = soma + n
        quant = quant + 1
    else:
        print('Programa sendo ecerrado.')
media = soma/quant
print('A qutantidade de números digitados é {}.\nA soma de números é {}. A média é {:.2f}.'.format(quant, soma, media))