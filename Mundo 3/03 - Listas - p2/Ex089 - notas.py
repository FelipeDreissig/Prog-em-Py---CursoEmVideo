dados = list()
aluno = list()
conjunto = list()
cri = ''
while True:
    nome = str(input('Qual o nome do aluno:')).strip().lower().capitalize()
    nota1 = int(input('Digite a primeira nota:'))
    nota2 = int(input('Digite a segunda nota:'))
    media = (nota1+nota2)/2
    dados.append(nota1)
    dados.append(nota2)
    dados.append(media)
    aluno.append(nome)
    aluno.append(dados[:])
    dados.clear()
    conjunto.append(aluno[:])
    aluno.clear()
    cri = str(input('Deseja continuar? [S/N]')).strip().lower()
    if cri == 'n':
        break
print(f'{"Nº":<4}{"Nome":<10}{"Nota media":>6}')
for i in range(0, len(conjunto)):
    print(f'{i+1:<4}{conjunto[i][0]:<10}{conjunto[i][1][2]:>6.2f}')
while True:
    p = int(input('Qual aluno você deseje verificar? (99 para sair)'))
    if p == 99:
        break
    print(f'{p:<4}{conjunto[p - 1][0]:<10}{conjunto[p - 1][1][2]:>6.2f}')
print('Até mais')



