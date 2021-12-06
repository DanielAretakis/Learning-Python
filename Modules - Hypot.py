from math import hypot
s1 = float(input('Type the first side of the right triangle to find the hypotenuse: '))
s2 = float(input('Type the second side: '))
h = math.hypot(s1, s2)
print('The hypotenuse of this triangle is {:.2f}cm'.format(h))