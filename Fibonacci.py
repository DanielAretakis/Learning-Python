number = int(input("Type how many numbers of fibonacci sequence do you want to see: "))
n1 = 0
n2 = 1
print(f'{n1} → {n2}', end='')
c = 3
while c <= number:
    n3 = n1+n2
    print(f' → {n3}', end='')
    n1 = n2
    n2 = n3
    c += 1