def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é de {a}m²')


# Programa Principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m) : '))
c = float(input('Comprimento (m) :'))
área(l, c)