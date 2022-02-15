t = 0
n = int(input('Type a whole number to see its times table: '))
for c in range(0, 10):
    print(f'|{n} x {t+1} = {n*(t+1)}|')
    t += 1