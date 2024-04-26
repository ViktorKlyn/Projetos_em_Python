frase = str(input('Digite uma frase : ')).upper().strip()
print('A letra (a) aparece : {} vezes na frase.'.format(frase.count('A')))
print('A letra (a) aparece pela primeira vez na : {}º posição.'.format(frase.find('A')+1))
print('A letra (a) aparece pela úlyima vez na posição : {}.'.format(frase.rfind('A')+1))