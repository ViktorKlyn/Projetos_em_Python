nome = str(input('Digite o seu nome completo : '))
print(nome.upper())
print(nome.lower())
print('Ao todo o seu nome tem : {} letras!'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem : {} letras!'.format(nome.find(' ')))