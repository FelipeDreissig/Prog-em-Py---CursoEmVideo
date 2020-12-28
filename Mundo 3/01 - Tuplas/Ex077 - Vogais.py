#vogais em aplavras
print('Digite palavras sem acento ou pontuação.')
pala1 = str(input('Digite uma palavra aleatória:')).strip().lower()
pala2 = str(input('Digite uma palavra aleatória:')).strip().lower()
pala3 = str(input('Digite uma palavra aleatória:')).strip().lower()
tupla = (pala1, pala2, pala3)
vogais = ('a', 'e', 'i', 'o', 'u')
for p in tupla:
    print(f'\nPara a palavra {p}, temos:')
    for i in range(1,len(p)):
        if p[i] in vogais:
            print(f'\033[7;31;40m{p[i]}, na {i+1}ª posição.\033[m')