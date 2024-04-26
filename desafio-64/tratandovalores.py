num = cont = som = 0
num = int(input('Digite o número [999] para acabar'))
while num != 999:
    som += num
    cont += 1
    num = int(input('Digite o número [999] para acabar'))
print('Você digitou {} números e a soma entre eles foi: {} '.format(cont, som))