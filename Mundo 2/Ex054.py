## maior e menor idade
from datetime import date
maior = 0
menor = 0
for x in range(1, 7, 1):
    nasc = int(input('Em que ano você nasceu?'))
    idade = date.today().year - nasc
    if idade>18:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoa(s) é(são) de maior idade.\n{} pessoa(s) é(são) de menor idade.'.format(maior, menor))
