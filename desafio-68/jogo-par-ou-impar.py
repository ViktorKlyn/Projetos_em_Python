from random import randint
v = 0
while True:
    jgd = int(input('Digite um número: '))
    comp = randint(0, 10)
    total = jgd + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jgd} e o computador jogou {comp}. Total de {total}', end='')
    print('. Deu Par' if total % 2 == 0 else '. Deu Ímpar')
    if tipo == 'P':
            if total % 2 == 0:
                print('Você Venceu!')
                v += 1
            else:
                print('Você Perdeu!')
                break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
    print(f'Game Over! Você venceu {v} vezes')