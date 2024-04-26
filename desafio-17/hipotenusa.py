ca = float(input('Valor do cateto adjacente : '))
co = float(input('Valor do cateto oposto : '))
hip = (ca ** 2 + co ** 2) ** (1/2)
print('O valor da hipotenusa é : {:.2f}'.format(hip))