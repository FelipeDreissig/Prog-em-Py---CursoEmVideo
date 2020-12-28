import requests
try:
    response = requests.get('http://pudim.com.br')
except:
    print('Deu ruim')
else:
    print('Tudo mara.')