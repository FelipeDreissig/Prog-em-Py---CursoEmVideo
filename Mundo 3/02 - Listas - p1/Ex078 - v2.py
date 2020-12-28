c = 0
l = []
for c in range(0, 5):
    n = int(input(f'Digite o {c + 1}º valor, sem repetir:'))
    while n in l:
        n = int(input(f'Digite o {c+1}º valor, sem repetir:'))
    l.append(n)
    n = ' '
print(f'O maior valor foi o {max(l)} na {l.index(max(l))+1}ª posição.\n'
      f'O menor valor foi o {min(l)} na {l.index(min(l))+1}ª posição.')