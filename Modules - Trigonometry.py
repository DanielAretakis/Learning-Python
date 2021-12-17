from math import radians, tan, cos, sin

angle = float(input('Type the angle value: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print('The sine of {}º is {:.2f}'.format(angle, sine))
print('The cosine of {} is {:.2f}'.format(angle, cosine))
print('The tangent of {} is {:.2f}'.format(angle, tangent))
