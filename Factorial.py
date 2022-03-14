from math import factorial

n = int(input('Digite um número para saber seu fatorial: '))
f = factorial(n)

'''
f = n
while n != 1:
    f = f * (n-1)
    n = n-1'''
print(f'O fatorial desse número é {f}')