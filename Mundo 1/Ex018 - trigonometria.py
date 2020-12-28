#### lendo um angulo qualquer
import math
angu = float(input('Digite um angulo qualquer, em graus: \n'))

ang = math.radians(angu)

print('Os graus digitados correspondem a {:.2f} radianos'.format(ang))

sen = math.sin(ang)
cos = math.cos(ang)
tg = math.tan(ang)

print('Os graus digitados são em seno {}, cosseno {} e tangente {}.'.format(sen, cos, tg))
