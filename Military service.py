from datetime import date

age = int(input('What is your year of birth? '))
n = date.today()
ay = n.year
y = (ay - age - 18) * -1
y2 = ay - age - 18
if ay - age > 18:
    print(f'You already passed the time to start the military service for {y2} year(s)!')
elif ay - age == 18:
    print('You have to start the military service this year!!')
elif ay - age < 18:
    print(f'You are ok, come back in {y} year(s)')