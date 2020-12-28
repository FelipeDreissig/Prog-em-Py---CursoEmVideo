#soma sem considerar o flag
l = j = 0
print('Digite 999 para parar.')
while True:
    c = int(input('Digite um número inteiro:\n'))
    if c != 999:
        j = j + c
        l = l + 1
    else:
        break
print(f'Fim do programa.\nA soma é {j} e foram digitados {l} números.')