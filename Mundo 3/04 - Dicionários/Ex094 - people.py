q = 0
pessoa = dict()
people = list()
somaidade = 0
mulheres = list()
pessoaacima = list()
while True:
    pessoa.clear()
    q = q + 1
    pessoa['name'] = str(input(f'Digite o nome da {q}ª pessoa:')).strip().lower().capitalize()
    while True:
        pessoa['years old'] = int(input(f'Digite a idade da {q}ª pessoa:'))
        if type(pessoa['years old']) == int or float:
            break
        print('Por favor, apenas valores numérios.')
    while True:
        pessoa['gender'] = str(input(f'Digite o sexo da {q}ª pessoa:\n'
                                     f'F - Feminino\n'
                                     f'M - masculino\n')).strip().lower()[0]
        if pessoa['gender'] in 'fm':
            break
        print('Por favor, digite apenas M ou F')
    people.append(pessoa.copy())
    while True:
        exit = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
        if exit in 'sn':
            break
        print('Por favor, apenas S ou N.')
    if exit == 'n':
        break
for k in people:
    somaidade = somaidade + k['years old']
    if k['gender'] == 'f':
        mulheres.append(k.copy())
mediaidade = somaidade/q
for y in people:
    if y['years old']>=mediaidade:
        pessoaacima.append(y.copy())
print(f'Foram cadastradas {q} pessoas.')
print(f'os cadastrados foram:\n{people}')
print(f'A média de idade é {mediaidade} anos.')
print(f'As mulheres cadastradas foram:\n{mulheres}')
print(f'As pessoas com idade igual ou maior da média são:\n{pessoaacima}')
