salario = float(input('Salário : R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Salário de R${:.2f} aumentou para : R${:.2f}'.format(salario, novo))