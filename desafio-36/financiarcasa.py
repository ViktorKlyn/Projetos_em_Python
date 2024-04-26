v = float(input('Valor da casa : R$ '))
s = float(input('Salário do comprador : R$ '))
a = int(input('Quantos anos de fianciamento : '))
p = v / (a * 12)
m = s * 30 / 100
print('Para pagar uma casa de R$ {:.3f} em {} anos '.format(v, a), end='')
print('A prestação será de : R$ {:.3f} '.format(p))
if p <= m:
    print('Empréstimo concedido! A sua parcela mensal será de : R$ {:.3f} '.format(p))
else:
    print('Empréstimo negado!')