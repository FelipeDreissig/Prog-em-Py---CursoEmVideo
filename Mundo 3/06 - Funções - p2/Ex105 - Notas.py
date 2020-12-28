def notas(*n, sit=False):
    s = ' '
    contador = 0
    maior = menor = n[0]
    for i in range(0, len(n)):
        contador = contador + n[i]
        if n[i] > maior:
            maior = n[i]
        if n[i] < menor:
            menor = n[i]
    media = contador/len(n)
    if sit:
        if 0 < media < 5:
            s = 'Péssima'
        if 5 <= media < 7:
            s = 'Ruim'
        if media >= 7:
            s = 'Bom'
        return {'total': contador, 'Maior': maior, 'menor': menor, 'media': media, 'situação': s}
    else:
        return {'total': contador, 'Maior': maior, 'menor': menor, 'media': media}


n1 = notas(5, 8, 7, 5, 6, sit=True)
print(n1)


