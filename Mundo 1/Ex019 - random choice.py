#### sorteando alunos
import random
n1 = str(input('O nome do primeiro aluno: '))
n2 = str(input('O nome do segundo aluno: '))
n3 = str(input('O nome do terceiro aluno: '))
n4 = str(input('O nome do quarto aluno: '))

lista = [n1, n2, n3, n4]

escolha = random.choice(lista)

print('Quem limpará a sala hoje é o(a) {}.'.format(escolha))