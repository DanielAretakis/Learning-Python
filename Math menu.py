from time import sleep

n1 = n2 = opt = 0

n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))

while opt != 5:
    opt = int(input('''[ 1 ] Sum
[ 2 ] Multiply
[ 3 ] Divide
[ 4 ] New numbers
[ 5 ] Bye bye
Your choice: '''))
    if opt == 1:
        print(f'{n1} plus {n2} is: {n1+n2}')
        sleep(2)
    if opt == 2:
        print(f'{n1} times {n2} is equal to: {n1*n2}')
        sleep(2)
    if opt == 3:
        print(f'{n1} divided by {n2} is: {n1/n2 :.2f}')
        sleep(2)
    if opt == 4:
        n1 = int(input('Type the new first number: '))
        n2 = int(input('Now, type the new second number: '))
        sleep(2)
    else:
        print('See you soon!')