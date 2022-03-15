from math import factorial

n = int(input('Type a number to see its factorial: '))
'''f = factorial(n)
print(f)'''
f = n
while n != 1:
    print(f'{n}', end='')
    print(' x ' if n > 2 else ' = ', end='')
    f *= (n-1)
    n -= 1
print(f'{f}')
