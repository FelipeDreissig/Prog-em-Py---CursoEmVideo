#### lista de produtos
menor = ' '
price = total = sum_cem = j = menorpreco = 0
print('-'*5, 'Lista de compras', '-'*5)
while True:
    c = nome = ' '
    nome = str(input('Nome do produto: ')).strip().title()
    price = int(input('Preço do produto: '))
    total = total + price
    j = j + 1
    if price>1000:
        sum_cem = sum_cem + 1
    if j==1:
        menorpreco = price
        menor = nome
    else:
        if price<menorpreco:
            menorpreco = price
            menor = nome
    while c not in 'sn':
        c = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if c=='n':
        break
print('Fim do programa')
print(f'Foram colocados na cesta {j} produtos.')
print(f'O total da compra é {total} reais.')
print(f'O total de produtos custando acima de mil é de {sum_cem}.')
print(f'O produto mais barato é o {menor}.E ele custa {menorpreco} reais.')

