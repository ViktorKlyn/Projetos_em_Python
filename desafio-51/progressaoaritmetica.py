a1 = int(input('Digit o 1º termo : '))
q = int(input('Digite a razão : '))
a10 = a1 + (10 - 1) * q
for c in range(a1, a10 + q, q):
    print('{} '.format(c), end='...')
print('Acabou!')