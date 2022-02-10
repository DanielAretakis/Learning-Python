from datetime import date

age = int(input('What is your year of birth? '))
n = date.today()
ay = n.year
y = (ay - age - 18) * -1
if ay - age > 18:
    print('You already passed the time to start the military service!')
elif ay - age == 18:
    print('You have to start the military service this year!!')
elif ay - age < 18:
    print(f'You are ok, come back in {y} year(s)')