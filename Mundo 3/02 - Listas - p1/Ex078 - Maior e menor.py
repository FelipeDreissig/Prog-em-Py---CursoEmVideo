### maior e menor em uma LISTA
posicoes = []
n1 = int(input('Digite um valor:\n'))
n2 = int(input('Digite outro valor:\n'))
n3 = int(input('Digite mais um valor:\n'))
n4 = int(input('Este é o penúltimo valor:\n'))
n5 = int(input('Digite o último valor:\n'))
lista = [n1, n2, n3, n4, n5]
maior = max(lista)
menor = min(lista)
for c, i in enumerate(lista):
    if i == maior:
        posicoes.insert(c,0)
    if i == menor:
        posicoes.insert(c,1)
print(f'O maior valor é o {maior} e ele está na {posicoes[0]}ª posição.')
print(f'O menor valor é o {menor} e ele está na {posicoes[1]}ª posição.')