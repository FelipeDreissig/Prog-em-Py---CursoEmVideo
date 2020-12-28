def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    :param n: O número que será feito o fatorial.
    :param show: Apresenta o cálculo ou não
    :return:o valor do fatorial.
    """
    c = 1
    for l in range(n, 0, -1):
        c = c*l
        if show:
            if l == 1:
                print(f' {l}', end='')
                print(' = ', end='')
            else:
                print(f' {l} x', end='')
    return c


print(fatorial(5, show=True))