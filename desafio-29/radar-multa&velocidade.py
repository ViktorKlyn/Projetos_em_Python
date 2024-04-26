v = float(input('Qual é a velocidade do veículo? '))
if v >80:
    print('!MULTADO! Velocidade acima do permitido!')
    m = (v - 80) * 7
    print('O valor da multa é : R$ {:.2f}!'.format(m))
print('Dentro do limite de velocidade.')
