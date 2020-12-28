import CursoEmVídeo.UtilidadesCeV

p = CursoEmVídeo.UtilidadesCeV.Dado.leiadado('Digite o preço: R$')
au = int(input('Qual o aumento?'))
des = int(input('Qual o desconto?'))
while True:
    f = str(input('Deseja formatar os números? [S/N]')).strip().lower()[0]
    if f == 'n':
        f = False
        break
    if f == 's':
        f = True
        break
CursoEmVídeo.UtilidadesCeV.Moeda.resumo(x=p, y=au, z=des, p=f)



## isto aqui está dentro da função resumo
"""print(f'O preço, acrescido de {au}% é de {Moeda.aumentarp(p, au, formato=f)}')
print(f'O preço, descontado de {des}% é de {Moeda.diminuirp(p, des, formato=f)}')
print(f'O dobro de {Moeda.moeda(p)} é de {Moeda.dobro(p, formato=f)}')
print(f'A metade de {Moeda.moeda(p)} é de {Moeda.metade(p, formato=f)}')"""
