dici = dict()
dici['nome'] = str(input('Qual o nome? ')).strip().lower().capitalize()
dici['media'] = int(input(f'Qual a média do(da) {dici["nome"]}? '))
if dici['media'] > 7:
    dici['situacao'] = 'aprovado'
else:
    dici['situacao'] = 'reprovado'
for k, v in dici.items():
    print(f' {k} é igual a {v}.')