#analisando pessoas
listapeso = list()
listanome = list()
listaa = list()
q = 0
nome = ''
peso = 0
maiores = list()
menores = list()
while True:
    nome = str(input(f'Digite o nome da {q+1}ª pessoa:'))
    peso = float(input(f'Digite o peso da {q+1}:ª pessoa:'))
    listaa.append(nome)
    listaa.append(peso)
    listapeso.append(peso)
    listanome.append(nome)
    nome = ''
    peso = 0
    q = q + 1
    cont = str(input('Deseja continuar?[S/N]')).strip().lower()[0]
    if cont == 'n':
        break
maior = max(listapeso)
menor = min(listapeso)
for p in range(0, len(listapeso)):
    if listapeso[p] == maior:
        maiores.append(listanome[p])
    if listapeso[p] == menor:
        menores.append(listanome[p])
print(f'Foram cadastradas {len(listaa)/2} pessoas.')
print(f'As pessoas (a pessoa) mais pesadas são(é):')
print(f'{maiores}', end=' ')
print(f'com {maior}Kg.')
print(f'As pessoas (a pessoa) mais leve(s) são(é):')
print(f'{menores}', end=' ')
print(f'com {menor}Kg.')


