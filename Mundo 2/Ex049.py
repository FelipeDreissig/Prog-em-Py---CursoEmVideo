#criando uma tabuada
tab = int(input('Você quer a tabualda de qual número?\n'))
print('================')
for c in range(0,11):
    cont = c*tab
    print('\033[0;7m {} X {} = {}\33[m'.format(tab, c, cont))
print('===============')




