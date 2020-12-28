def voto(n):
    from datetime import datetime
    idade = datetime.now().year - n
    if idade < 16:
        return f'Com {idade} anos, você não vota.'
    elif 16 <= idade < 18:
        return f'Com {idade} anos, o voto é opcional.'
    elif 18 <= idade < 70:
        return f'Com {idade} anos, o voto é obrigatório.'
    else:
        return f'Com {idade} anos, o voto é opcional.'


nas = int(input('Digite o ano de nascimento:'))
print(voto(nas))
