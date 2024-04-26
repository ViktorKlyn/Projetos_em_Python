from random import randint
cpt = randint(0, 5)
print('Vou pensar de um número de (0 à 5)...! Tente adivinhar... ')
jgd = int(input('Em que número pensei? '))
print('PROCESSANDO... ')
if jgd == cpt:
    print('Parabéns! Você me venceu! ')
else:
    print('Ganhei! Eu pensei no número {} !'.format(cpt))