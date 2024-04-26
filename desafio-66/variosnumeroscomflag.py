soma = cont = 0
while True:
    num = int(input('Digite o número [999] para encerrar'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} números foi {soma}')