spd = int(input('Type the speed of the car: '))
if spd > 80:
    tax = (spd-80)*7
    print('The person has to pay a total of ${}.00, because he/she passed the speed limit!'.format(tax))
else:
    print('That is ok, it is on the speed limit')