from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR 
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Escolher opção:  '))
    if opcao == 1:
     soma = n1 + n2
     print('{} + {} = {} '.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('{} x {} = {} '.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {}, o maior valor é: {} '.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digit eos 2º valor: '))
    elif opcao == 5:
        print('Finalizando... ')
    else:
        print('Opção inválida! Tente novamente ')
    print('-' * 50)
    sleep(1)
print('Fim do programa!')