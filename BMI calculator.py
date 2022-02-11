height = float(input('''To start the BMI calculator, I'm gonna need your height and your weight
First, type your height in metres or centimetres: '''))
weight = float(input('Now, type your weight: '))
bmi = weight/height**2
if bmi < 18.5:
    print('You are underweight, be careful!')
elif bmi > 18.5 and bmi < 25:
    print('You are at the normal weight, nice!!!')
elif bmi > 25 and bmi < 30:
    print('You are with overweight, be careful!')
elif bmi > 30 and bmi < 40:
    print('You are at the obesity group, be really careful!!')
else:
    print('You are at obesity class 3, look for help!')