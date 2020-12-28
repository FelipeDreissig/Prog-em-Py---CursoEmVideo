def LeiaInte(n):
    while True:
        try:
            k = int(input(n))
        except (ValueError, TypeError):
            print('Por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            k = 0
            return k
        else:
            return k




def LeiaFloat(n):
    while True:
        try:
            k = str(input(n)).replace(',', '.')
            k = float(k)
        except (ValueError, TypeError):
            print('Por favor, digite um número válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            k = 0
            return k
        else:
            return k


i = LeiaInte('Digite um número inteiro: ')
r = LeiaFloat('Digite um número real: ')
print(f'Os valos digitados foram {i} e {r}')

