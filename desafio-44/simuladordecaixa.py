print('{:=^40} '.format(' LOJAS TIGER '))
p = float(input('Preço das compras : R$ '))
print('''Formas de pagamento :
[ 1 ] à vista no dinheiro ou cheque.
[ 2 ] à vista no cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão. ''')
opc = int(input('Opção : '))
if opc == 1:
    total = p - (p * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(p, total))
elif opc == 2:
    total = p - (p * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(p, total))
elif opc == 3:
    total = p
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS! '.format(parcela))
elif opc == 4:
    total = p + (p * 20 / 100)
    totpar = int(input('Quantas parcelas? '))
    parcela = total / totpar
    print('Sua compra será pareclada em {}x de R${:.2f} COM JUROS! '.format(totpar, parcela))
else:
    total = p
    print('Opçao inválida de pagamento! Tente novamente. ')