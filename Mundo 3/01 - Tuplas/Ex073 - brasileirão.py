# tabela do brasileirão - inventarei uma tabela obs:brasileiro nao começou
tupla = ('grêmio', 'flamengo', 'vasco', 'internacional', 'chapecoense', 'fluminense', 'avai', 'athletico', 'atletico', 'palmeiras', 'são paulo', 'corinthians', 'santos', 'botafogo', 'bahia', 'ceara', 'ponte preta', 'juventude','guarani', 'cruzeiro')
order = sorted(tupla)
posichape = tupla.index('chapecoense')
print(f'Os 5 primeiros colocados são, {tupla[:5]}.\n')
print(f'Os últimos 4 colocados são, {tupla[16:]}.\n')
print(f'A tabela, em ordem alfabética é, {order}.\n')
print(f'A chapecoense está na {posichape+1}ª posição.')
