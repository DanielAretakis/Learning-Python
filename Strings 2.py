number = int(input('Type a number from 0 to 9999: '))
unity = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10
print('Thousand: {}'.format(thousand))
print('Hundred: {}'.format(hundred))
print('Ten: {}'.format(ten))
print('Unity: {}'.format(unity))
