#### criar um algoritmo que mostre o antecessor e o sucessor de um número escolhido
num = int(input("Digite um número qualuqer: "))
print('O número escolhido é {}.'.format(num))
ant = num - 1
suc = num + 1
print('O sucessor do número escolhido é {} e o antecessor é {}.'.format(suc, ant))