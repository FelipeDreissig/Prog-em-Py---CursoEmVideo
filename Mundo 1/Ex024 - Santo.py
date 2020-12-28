#### verificando se o nome da cidade posssui 'Santo'
cid = str(input('Digite o nome de uma cidade: \n'))
cid2 = list(cid.split())
cid2 = cid2[0]
comec = cid2.upper()
t = 'SANTO' in comec
print('A cidade começa com o nome Santo? \n {}'.format(t))
