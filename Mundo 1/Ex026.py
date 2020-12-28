## quantas vezes apareceu uma letra em uma frase e a posição da primeira e da última vez

frase = str(input('Digite uma frase qualquer: \n')).strip()
fraseaux = frase.upper()
print("A letra 'A' aparece \n{} vezes".format(fraseaux.count('A')))
print("A primeira vez que aparece a letra 'A' é na posição: \n {}".format(fraseaux.find('A')+1))
print("A última vez que aparece a letra 'A' é na posição: \n {}".format(fraseaux.rfind('A')+1))
