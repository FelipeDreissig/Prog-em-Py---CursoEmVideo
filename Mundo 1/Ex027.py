###### primeiro e último nome
nome = str(input('Digite seu nome completo: \n'))
nome = list(nome.strip().title().split())
tam = len(nome)-1
print('O seu primeiro nome é: \n{}\nO seu último nome é:\n{}'.format(nome[0], nome[tam]))