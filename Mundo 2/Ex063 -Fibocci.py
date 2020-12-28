# sequência de fibonacci
fim = int(input('Quantos números de fibonacci você quer ver? '))
c = 0
a = 0
b = 1
fibo = a + b
print('{}\n{}'.format(a, b))
while fim!=c:
    print('{}'.format(fibo))
    a = b
    b = fibo
    fibo = a + b
    c = c + 1