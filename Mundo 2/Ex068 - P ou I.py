#### jogando par ou ímpar
import random
print('Jogando par ou ímpar')
c = 0
while True:
    alternatiras = (1,2,3,4,5,6,7,8,9,10)
    escolha = int(random.choice(alternatiras))
    n = int(input('Escolha um número inteiro:'))
    total = escolha + n
    modelo = str(input('Você deseja par ou ímpar? [P/I]')).strip().lower()[0]
    if total%2==0 and modelo=='p':
        c = c + 1
        print(f'Você escolheu {n} e o computador escolheu {escolha}.\nA soma deu {total}\n')
        print('Parabéns, você ganhou.')
    elif total%2!=0 and modelo=='p':
        print(f'Você escolheu {n} e o computador escolheu {escolha}.\nA soma deu {total}\n')
        print('Voce perdeu.\n')
        if c!=0:
            print(f'Você opteve {c} vitória(s).')
        break
    elif total%2!=0 and modelo=='i':
        c = c + 1
        print(f'Você escolheu {n} e o computador escolheu {escolha}.\nA soma deu {total}\n')
        print('Parabéns, você ganhou.')
    elif total%2==0 and modelo=='i':
        print(f'Você escolheu {n} e o computador escolheu {escolha}.\nA soma deu {total}\n')
        if c!=0:
            print(f'Voce perdeu.\nVoce obrteve {c} vitória(s).')
        break
