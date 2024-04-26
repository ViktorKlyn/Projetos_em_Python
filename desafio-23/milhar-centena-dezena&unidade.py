num = int(input('Digite algum número : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Milhar : {}'.format(m))
print('Centena : {} '.format(c))
print('Dezena : {} '.format(d))
print('Unidade : {} '.format(u))
