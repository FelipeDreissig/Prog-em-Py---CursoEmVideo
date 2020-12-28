jogador = dict()
jogador['nome'] = str(input('Digite o nome do jogador:')).strip().lower().capitalize()
p = int(input('Qual a posição do jogador:\n'
              '1 - Defensor\n'
              '2 - Meio-campo\n'
              '3 - Atacante\n'))
if p == 1:
    jogador['posição'] = 'Defensor'
elif p == 2:
    jogador['posição'] = 'Meio-campo'
else:
    jogador['posição'] = 'atacante'
jogador['jogos'] = int(input('Digite o total de jogos válidos na carreira:'))
jogador['Gols'] = int(input('Digite a quantidade de gols nos jogos válidos:'))
jogador['Assistência'] = int(input('Digite a quantidade de assistências:'))
jogador['Decisoes'] = int(input('Quantos jogos eram finais?'))
for i in range(1, jogador['Decisoes']+1):
    jogador[f'Decisão {i}'] = int(input(f'Na {i}ª final, quantas assistências e gols foram feitos (somados):'))
for t, k in jogador.items():
    print(t, '=', end=' ')
    print(k)
print(f'O aproveitamento na carreira do(a) {jogador["nome"]} foi de {(jogador["Gols"]+jogador["Assistência"])/jogador["jogos"]:.2f}.')
aproveitamento = 0
for i in range(1, jogador['Decisoes']+1):
    aproveitamento = aproveitamento + jogador[f'Decisão {i}']
print(f'O aproveitamento do(a) {jogador["nome"]} nas finais foi de:{aproveitamento/jogador["Decisoes"]:.2f}.')
