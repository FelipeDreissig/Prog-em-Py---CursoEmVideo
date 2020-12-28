esp = str(input('Digite uma expressão matemática:')).strip().lower()
abre = 0
n = 0
fecha = 0
for x in range(0, len(esp)):
    if esp[x]=='(':
        abre = abre + 1
    if esp[x]==')':
        fecha = fecha + 1
        if abre==0 and fecha!=0:
            print('Sua expressão não está correta.')
            n = 97
            break
if n != 97:
    if abre==fecha:
        print('A expressão está correta.')
    else:
        print('A expressão está errada.')
        if abre<fecha:
            print('Você precisa abriu menos parênteses do que fechou.')
        else:
            print('Você abriu mais parênteses do que fechou.')
if n==97:
    print('Não é possível começar uma equação fechando parênteses.')
