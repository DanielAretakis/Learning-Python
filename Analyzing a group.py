ta = 0
oma = 0
om = ''
c = 0
for g in range(1, 5):
    name = input(f'Type the name of the person number {g}: ')
    age = int(input('Now his/her age: '))
    ta += age
    gender = input('And the gender: M/F ').upper().strip()
    if gender == 'M':
        if g == 1:
            oma = age
            om = name
        if age > oma:
            oma = age
            om = name
    else:
        if age < 20:
            c += 1

print(f'The average age of the group is {ta/4}')
print(f'The oldest man is {om} with {oma} years')
print(f'We have {c} women under 20 years old')
