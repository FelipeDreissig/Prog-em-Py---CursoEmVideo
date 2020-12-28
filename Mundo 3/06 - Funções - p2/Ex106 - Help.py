def cabeçalho(x):
    print('\033[7;34;40m-\033[m' * len(x))
    print(f'\033[7;34;40m{  x  }\033[m')
    print('\033[7;34;40m-\033[m' * len(x))


def desespero(k):
    cabeçalho(k)
    help(k)

while True:
    cabeçalho('ajuda interativa')
    ajuda = str(input('\033[7;30;41mDigite a função ou comando que precisa de ajuda (digite fim para encerrar):\033[m\n')).strip().lower()
    if ajuda == 'fim':
        print('Até a próxima')
        break
    desespero(ajuda)







