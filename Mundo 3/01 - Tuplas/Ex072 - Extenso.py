# número por extenso
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeros = (0, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
num = int(input('Digite um número de 0 a 20:'))
while num not in numeros:
    num = int(input('Tente novamente. Digite um número de 0 a 20:'))
print(f'Vode digitou o número {tupla[num]}.')