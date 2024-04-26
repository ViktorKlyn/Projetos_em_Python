resp = 'S'
soma = quan = med = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número'))
    soma += num
    quan += 1
    if quan == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
            if num < menor:
                menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
med = soma / quan
print('Você digitou {} números e a média foi: {}'.format(quan, med))
print('O maior valor foi: {} e o menor foi: {}'.format(maior, menor))
