from random import randint
computador = randint(0, 1001)
print('Acabei de pensar em um número em um número de: (0 à 1000 ')
print('Será que você consegue adivinhar? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS, Tente Novamente ')
        elif jogador > computador:
            print('MENOS... Tente Novamente ')
print('Você acretou com {} tentativas '.format(palpite))