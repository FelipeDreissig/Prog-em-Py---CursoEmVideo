def leiadado(k):
    j = str(input(k)).strip().replace(',', '.')
    p = j.replace('.', '')
    while True:
        if not p.isnumeric():
            print(f'Erro, "{j}" não é um valor númerico.')
            j = str(input('Digite o preço: R$')).replace(',', '.')
            p = j.replace('.', '')
        else:
            j = float(j)
            break
    return j

