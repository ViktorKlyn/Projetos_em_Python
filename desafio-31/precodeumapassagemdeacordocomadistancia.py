d = int(input('Qual é a distância da viagem? '))
p = d * 0.5 if d <= 200 else d * 0.45
print('O preço da passagem é : R$ {:.2f}'.format(p))
