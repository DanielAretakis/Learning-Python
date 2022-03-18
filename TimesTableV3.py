while True:
    n = int(input('Type a whole number to see its times table: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n :2} x {c :2} = {n * (c) :2}')
print('Bye, see you soon!')
