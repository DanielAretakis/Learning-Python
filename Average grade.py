n1 = float(input('Type the first test grade: '))
n2 = float(input('Type the second teste grade: '))
a = (n1+n2)/2
if a >= 7:
    print('Congratulations you passed!!')
elif a >= 5 and a < 7:
    print('You need to do the final test!')
elif a < 5:
    print('You failed this year, sorry.')