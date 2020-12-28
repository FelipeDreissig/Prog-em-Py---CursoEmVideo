### verificando se uma frase é um políndromo
frase = str(input('Digite a frase:\n')).strip().lower()
sep = frase.split()
junto = ''.join(sep)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso =inverso + junto[letra]
if inverso==junto:
    print('É um políndromo.')
    print(junto)
    print(inverso)
else:
    print('Não é um políndromo.')
    print(junto)
    print(inverso)