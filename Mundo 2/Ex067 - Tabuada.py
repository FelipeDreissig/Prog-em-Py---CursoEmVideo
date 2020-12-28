### fazendo uma tabuada
while True:
    n = int(input('Voce quer a tabuada de qual número:\n'))
    if n<0:
        print('Tabuada de números negativos não é válido.')
        break
    for aux in range(0,11):
        resultado = n*aux
        print(f'\033[1;32m* {n} X {aux} = {resultado}\033[m')