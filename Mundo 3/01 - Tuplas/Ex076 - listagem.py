# lista de produtos
tupla = ('Sabonete', 2.99, 'Xampu', 5.50, 'Pão de sal', 5, 'Frios', 4.50, 'Café', 4.19)
print('\033[31;40mproduto', '-'*(12), '==', 'Preço\033[m')
for c in range(0, len(tupla), 2):
    pos = tupla.index(tupla[c])
    print(f'{tupla[c]:.<20} == {tupla[pos+1]}')
