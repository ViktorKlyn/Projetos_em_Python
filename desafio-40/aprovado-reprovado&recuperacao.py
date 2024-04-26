n1 = float(input('Primeira nota : '))
n2 = float(input('Segunda nota : '))
s1 = n1 + n2
s2 = s1 / 2
print('A média das notas {:.1f} + {:.1f} é igual a : {:.1f} '.format(n1, n2, s2))
if 6> s2 >=5:
    print('Recuperação! ')
elif s2 <5:
    print('Reprovado! ')
elif s2 >=6:
    print('Aprovado! ')