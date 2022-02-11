s1 = int(input('Type the first side of the triangle: '))
s2 = int(input('Now the second side: '))
s3 = int(input('And the third: '))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    if s1==s2 or s2==s3 or s1==s3:
        if s1==s2 and s1!=s3:
            print('It is an isosceles triangle')
        elif s1==s3 and s1!=s2:
            print('It is an isosceles triangle')
        elif s2==s3 and s2!=s1:
            print('It is an isosceles triangle')
        else:
            print('It is an equilateral triangle')
    elif s1!=s2 and s1!=s3 and s2!=s3:
        print('It is an scalene triangle')
else:
    print("Can't form a triangle")