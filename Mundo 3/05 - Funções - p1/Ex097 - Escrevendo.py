def escreva(t):
    k = len(t) + 4
    print('-'*k)
    print(f'  {t}')
    print('-'*k)


n = str(input('O que deseja que seja escrito?')).strip().lower().title()
escreva(n)