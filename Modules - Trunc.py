from math import trunc
num = float(input('Type a float number: '))
print('The int part of {} is {}'.format(num, trunc(num)))
#I could use int(num) instead of trunc