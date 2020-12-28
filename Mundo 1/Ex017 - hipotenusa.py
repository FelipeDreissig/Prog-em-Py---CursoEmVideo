# calculando a hipotenusa
import math
cat1 = float(input('Qual o valor de um dos catetos: '))
cat2 = float(input('Qual o valor do outro cateto: '))
hipotenusa = float(math.hypot(cat1, cat2))
print('A hipotenusa é de {:.2f}'.format(hipotenusa))