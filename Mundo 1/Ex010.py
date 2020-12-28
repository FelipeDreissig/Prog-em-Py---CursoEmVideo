# convertendo reais em dólares
print('Olá, vamos converter reais em dólares,\n'
      'para começar, preciso de informações suas.')
riq = float(input('Quantos reais você quer converter? R$ \n'))
dol = float(input('Qual a cotação vigente?\n'))
total = riq/dol
print('Você terá {:.2f} dolares'.format(total))