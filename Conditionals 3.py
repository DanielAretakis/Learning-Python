from datetime import date
year = int(input('Type a year and I will say if its a leap year or not (Type 0 to use the the current year): '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Yes! {} is a leap year!'.format(year))
else:
    print('No, {} is not a leap year!'.format(year))