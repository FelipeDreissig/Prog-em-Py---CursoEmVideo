def area(a, b):
    ar = a*b
    print(f'A área do terro é de {ar:.1f} metros².')


# programa principal
l = float(input('Qual a largura do terreno?'))
c = float(input('Qual o comprimento do terreno?'))
area(l, c)
