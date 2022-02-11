n1 = float(input('Type the first number to compare: '))
n2 = float(input('Type the second number: '))
if n1>n2:
    print(f'{n1} is a higher number than {n2}')
elif n2>n1:
    print(f'{n2} is a higher number than {n1}')
elif n1==n2:
    print(f'{n1} and {n2} are equal')