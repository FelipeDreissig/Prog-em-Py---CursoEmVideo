#### posicionamento sem usar o sort, neste caso, usando o insert

l = []
p = 0
while True:
    n = int(input('Digite um número inteiro:'))
    if len(l)==0:
        l.append(n)
    elif len(l)==1:
        if n>=l[0]:
            l.insert(1, n)
        else:
            l.insert(0, n)
    elif len(l)==2:
        if n>=l[0] and n<=l[1]:
            l.insert(1, n)
        elif n<=l[0]:
            l.insert(0, n)
        else:
            l.append(n)
    elif len(l)==3:
        if n<=l[0]:
            l.insert(0, n)
        elif n>=l[0] and n<=l[1]:
            l.insert(1,n)
        elif n>=l[1] and n<=l[2]:
            l.insert(2, n)
        else:
            l.append(n)
    elif len(l)==4:
        if n<=l[0]:
            l.insert(0, n)
            break
        elif n>=l[0] and n<=l[1]:
            l.insert(1,n)
            break
        elif n>=l[1] and n<=l[2]:
            l.insert(2, n)
            break
        elif n>=l[2] and n<=l[3]:
            l.insert(3, n)
            break
        else:
            l.append(n)
            break
print(f'Os números digitados são, em ordem alfabética, {l}')
