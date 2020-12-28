### soma de números
print('Iremos somar números ímpares que são múltiplos de 3')
s = 0
p = 0
for c in range(1,501,2):
    print(c, end=' ')
    if c%3==0:
        p = p + 1
        s = s + c
print('\nA soma de todos os números ímpares que são múltiplos de 3 é {}.\n O total de números múltiplos é {}.'.format(s, p))