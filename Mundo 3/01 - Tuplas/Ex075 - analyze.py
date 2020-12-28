# analize de números

n1 = int(input('Digite um número inteiro:\n'))
n2 = int(input('Digite outro número inteiro:\n'))
n3 = int(input('Digite mais um número inteiro:\n'))
n4 = int(input('Digite o último número inteiro:\n'))
tupla = (n1, n2, n3, n4)
c = tupla.count(9)
print(f'Voce digitou os valores: {tupla}')
print(f'Apareceu {c} vez(es) o número nove.')
if 3 in tupla:
    print(f'O valor 3 apareceu na posição {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram:')
for num in tupla:
    if num%2==0:
        print(num, end=' ')
