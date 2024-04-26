a = int(input('Primeiro número : '))
b = int(input('Segundo número : '))
c = int(input('Terceiro número : '))
me = a
if b < a and b < c:
    me = b
if c < a and c < b:
        me = c
        ma = a
if b > a and b > c:
            ma = b
if c > a and c > b:
                ma = c
print('O menor valor digitado foi : {}'.format(me))
print('O maior valor digitado foi : {}'.format(ma))
