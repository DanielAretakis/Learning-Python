import random
n1 = int(input('Try to match the number between 1-5: '))
n2 = random.randint(1, 5)
if n1==n2:
    print('Nice job!')
else:
    print('Sorry, not this time, try again! The number was {}'.format(n2))