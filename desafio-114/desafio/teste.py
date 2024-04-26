import urllib.request
from urllib.error import URLError

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read().decode('utf-8'))  # Decode para exibir o conteúdo como texto
