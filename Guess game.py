from random import randint

number = randint(1, 10)
tries = 0
c = 1
while tries != number:
    tries = int(input('Try to guess the number I am thinking...: '))
    if tries != number:
        c += 1
        if tries > number:
            print('Try a lower number!')
        if tries < number:
            print('Try a higher number!')
if c != 1:
    print(f"Congratulations!! But you needed {c} tries, why don't you try to guess faster this time?")
else:
    print("Nice job, you made it on the first try, congratulations!!")