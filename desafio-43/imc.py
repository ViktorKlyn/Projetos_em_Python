p = float(input('Peso : (Kg) '))
a = float(input('Altura : (m) '))
imc = p / (a ** 2)
print('O IMC é igual a : {:.1f} '.format(imc))
if imc < 18.5:
    print('Abaixo do peso ideal! ')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal! ')
elif imc > 25 and imc <= 30:
    print('Acima do peso! ')
elif imc > 30 and imc <= 40:
    print('Obesidade! ')
elif imc > 40:
    print('Obesidade mórbida!')