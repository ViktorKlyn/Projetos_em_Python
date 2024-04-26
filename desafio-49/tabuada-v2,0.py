from time import sleep
num = int(input('Digite algum valor para ver a sua tabuada: '))
for c in range(0, 11):
    sleep(0.5)
    print('{} x {:2} = {} '.format(num, c, num*c))
