base = int(input('Type a full number: '))
print('''Select a base to convert your number
[ 1 ] Binary
[ 2 ] Octal
[ 3 ] Hexadecimal''')
option = int(input('Your choice: '))
if option == 1:
    print(f'{base} in binary is {bin(base)[2:]}')
elif option == 2:
    print(f'{base} in octal is {oct(base)[2:]}')
elif option == 3:
    print(f'{base} in hexadecimal is {hex(base)[2:]}')
else:
    print("I don't have this option")