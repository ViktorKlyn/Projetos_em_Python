from datetime import date
atual = date.today().year
a = int(input('Ano de nascimento : '))
idade = atual - a
print('Quem nasceu em {} tem {} anos em {} '.format(a, idade, atual))
if idade == 18:
    print('Você deve se alistar esse ano!')
elif idade <18:
    print('Você vai se alistar em {}! '.format(atual + (18 - idade)))
elif idade >18:
    print('Você já deveria ter se alistado em {}! '.format(atual - (idade - 18)))
