r1 = float(input('Primeiro seguimento : '))
r2 = float(input('Segundo seguimento : '))
r3 = float(input('Terceiro seguimento : '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO ')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO ')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima não podem formar um triângulo! ')