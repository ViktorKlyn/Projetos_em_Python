from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nas = int(input('Ano de nascimento: '.format(pess)))
    idade = atual - nas
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} pessoas maiores de idade '.format(totmaior))
print('E temos {} pessoas menores de idade '.format(totmenor))