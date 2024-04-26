print('Analizador de Triângulos.')
v1 = float(input('Primeiro seguimento : '))
v2 = float(input('Segumdo seguimento : '))
v3 = float(input('Terceiro seguimento : '))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
 print('Os seguimentos acima podem formar um triângulo! ')
else:
 print('Os seguimentos acima não podem formar uma triângulo! ')
