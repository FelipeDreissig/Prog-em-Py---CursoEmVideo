### calculando a média
n1 = float(input('Digite a nota um:\n'))
n2 = float(input('Digite a nota dois:\n'))
media = (n1+n2)/2
if media>=7:
    print('Sua média foi de {}. Está aprovado'.format(media))
elif media>=5 and media<7:
    print('Sua média foi de {}. Você está de recuperação.'.format(media))
else:
    print('Sua média foi de {}. Você está reporvado'.format(media))