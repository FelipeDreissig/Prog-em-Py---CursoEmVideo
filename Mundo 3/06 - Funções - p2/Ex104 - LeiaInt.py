def LeiaInte(n):
    j = input(n)
    if not j.isnumeric():
        while True:
            print('\033[7;34;40mErro. Digite um número inteiro.\033[m')
            j = input('Digite um número:')
            if j.isnumeric():
                j = int(j)
                return j
    else:
        j = int(j)
        return j


q = LeiaInte('Digite um número:')
print(f'O número digitado foi {q}.')