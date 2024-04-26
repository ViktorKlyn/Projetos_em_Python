from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura ')
pc = randint(0, 2)
print('''Suas opções :
[ 0 ] PEDRA.
[ 1 ] PAPEL.
[ 2 ] TESOURA. ''')

jgd = int(input('Qual a sua jogada? '))

print('JO ')
sleep(0.5)
print('KEN ')
sleep(0.5)
print('PO')

if jgd == 0 and pc == 2 or jgd == 1 and pc == 0 or jgd == 2 and pc == 1:
    print('-=' * 20)
    print('''COMPUTADOR ESCOLHEU : {}
JOGADOR ESCOLHEU : {}
JOGADOR VENCEU!'''.format(itens[pc], itens[jgd]))
    print('-=' * 20)

elif jgd == 0 and pc == 1 or jgd == 1 and pc == 2 or jgd == 2 and pc == 0:
    print('-=' * 20)
    print('''COMPUTADOR ESCOLHEU : {}
JOGADOR ESCOLHEU : {}
COMPUTADOR VENCEU!'''.format(itens[pc], itens[jgd]))
    print('-=' * 20)

elif jgd == pc:
    print('-=' * 20)
    print('''COMPUTADOR ESCOLHEU : {}
JOGADOR ESCOLHEU : {}
EMPATE!.'''.format(itens[pc], itens[jgd]))
    print('-=' * 20)

else:
    print('-=' * 23)
    print('JOGADA INVÁLIDA! TENTE SOMENTE ENTRE 0 à 2!')
    print('-=' * 23)