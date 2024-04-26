from math import radians, sin, cos, tan
a = float(input('Digite o ângulo :'))
seno = sin(radians(a))
print('O ângulo de {}º tem o seno de : {:.2f}º'.format(a, seno))
cosseno = cos(radians(a))
print('O ângulo de {}º tem o cosseno de : {:.2f}º'.format(a, cosseno))
tangente = tan(radians(a))
print('O ângulo de {}º tem a tangente de {:.2f}º'.format(a, tangente))
