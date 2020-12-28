def aumentarp(x, k=False, formato=False):
    if formato:
        if k or 0:
            t = (k/100) + 1
            j = t * x
            return f'R$ {j:.2f}'.replace('.', ',')
        else:
            k = 10
            t = (k / 100) + 1
            j = t * x
            return f'R$ {j:.2f}'.replace('.', ',')
    else:
        if k:
            t = (k/100) + 1
            j = t * x
            return j
        else:
            k = 10
            t = (k / 100) + 1
            j = t * x
            return j


def diminuirp(x, k, formato=False):
    if formato:
        if k or 0:
            t = 1 - (k / 100)
            j = t * x
            return f'R$ {j:.2f}'.replace('.', ',')
        else:
            k = 10
            t = 1 - (k / 100)
            j = t * x
            return f'R$ {j:.2f}'.replace('.', ',')
    else:
        if k:
            t = 1 - (k / 100)
            j = t * x
            return j
        else:
            k = 10
            t = 1 - (k / 100)
            j = t * x
            return j


def dobro(p, formato=False):
    if formato:
        p = p*2
        return f'R$ {p:.2f}'.replace('.', ',')
    else:
        p = p * 2
        return p


def metade(p, formato=False):
    if formato:
        p = p/2
        return f'R$ {p:.2f}'.replace('.', ',')
    else:
        p = p / 2
        return p


def moeda(k, formato=False):
    return f'R$ {k:.2f}'.replace('.', ',')


def resumo(x, y, z, p=False):
    if p:
        print(f'O preço \t\t\t\t\t{moeda(x)}')
        print(f'O preço com {y}% com aumento {aumentarp(x, y, True)}')
        print(f'O preço com {z}% desconto \t{diminuirp(x, z, True)}')
        print(f'O dobro de {moeda(x)} \t\t{dobro(x, True)}')
        print(f'A metade de {moeda(x)} \t\t{metade(x, True)}')
    else:
        print(f'O preço\t\t\t\t\t\t\t{x}')
        print(f'O preço com {y}% com aumento\t\t{aumentarp(x, y, False):.2f}')
        print(f'O preço com {z}% desconto\t\t{diminuirp(x, z, False):.2f}')
        print(f'O dobro de {x}\t\t\t\t{dobro(x, False)}')
        print(f'A metade de {x}\t\t\t\t{metade(x, False)}')

