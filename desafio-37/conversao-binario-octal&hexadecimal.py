n = int(input('Digite um número inteiro : '))
print('''Escolha uma das bases para a conversão :
[ 1 ] converter para BINÁRIO.
[ 2 ] converter para OCTAL.
[ 3 ] converter para HEXADECIMAL. ''')
opc = int(input('Escolha sua opção : '))
if opc == 1:
    print('{} convertido para BINÁRIO é igual a : {} '.format(n, bin(n)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL é igual a : {} '.format(n, oct(n)[2:]))
elif opc == 3:
 print('{} convertido para HEXADECIMAL é igual a : {} '.format(n, hex(n)[2:]))
else:
    print('Opção inválida! Tente novamente. ')