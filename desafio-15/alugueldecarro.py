dia = int(input('Total de dias alugado : '))
km = float(input('Total de km rodados '))
# dia = R$ 60,00
# km = R$ 0,15
p = (dia * 60) + (km * 0.15)
print('O total a ser pago é de : R$ {:.2f}'.format(p))