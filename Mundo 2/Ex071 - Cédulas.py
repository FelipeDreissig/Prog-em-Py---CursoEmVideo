# contando cédulas
print('\033[7;31;40m--- Banco Python ---\033[m')
while True:
    din = int(input('Quanto você deseja sacar?\n'))
    notas50 = int(din/50)
    resto1 = din - notas50*50
    notas20 = int(resto1/20)
    resto2 = resto1 - notas20*20
    notas10 = int(resto2/10)
    resto3 = resto2 - notas10*10
    notas1 = int(resto3/1)
    resto4 = resto3 - notas1
    if resto4==0:
        break
total = notas50 + notas20 + notas10 + notas1
print('\033[7;31;40mObrigado por trabalhar conosco, volte sempre.\033[m')
print(f'São necessárias {total} cédulas para esse saque;')
if notas50!=0:
    print(f'A quantidade de notas de 50 é de {notas50}.')
if notas20!=0:
    print(f'A quantidade de notas de 20 é de {notas20}.')
if notas10!=0:
    print(f'A quantidade de notas de 10 é de {notas10}.')
if notas1!=0:
    print(f'A quantidade de notas de 1 é de {notas1}.')



