numeros = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso! ')
    else:
        print('Valor duplicado! Não vou adicionar!')
        r = (int(str('Quer continuar? [ S / N ] ')))
        if r in 'Nn':
            break
print('-=' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')