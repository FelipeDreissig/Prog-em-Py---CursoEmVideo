def ficha(n=False, gol=False):
    if not n or n == '':
        n = '<desconhecido>'
    if not gol or gol == '':
        gol = 0
    print(f'O jogador {n} fez {gol} gol(s) na carreira.')


nome = str(input('Digite o nome do jogador:')).strip().lower().title()
g = input('Digite a quantidade de gols:')
if not g.isnumeric():
    while True:
        print('Digite apenas números.')
        g = input('Digite a quantidade de gols:')
        if g.isnumeric():
            break
ficha(nome, g)