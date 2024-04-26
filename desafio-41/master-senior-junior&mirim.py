from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento : '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos. '.format(ano, idade))
if idade <=9:
    print('Classificação : MIRIM. ')
if idade >= 10 and idade <= 14:
        print('Classificação : INFANTIL. ')
elif idade >= 15 and idade <=17:
          print('Classificação : JÚNIOR. ')
elif idade >= 18 and idade <= 24:
     print('Calssificação : SÊNIOR. ')
elif idade >= 25:
        print('Classificação : MASTER. ')