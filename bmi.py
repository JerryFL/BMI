height = input('please input your height, in meter :')
height = float(height)
weight = input('please input your weight, in kilogram :')
weigth = int(weight)
BMI = height / weight ^ 2
BMI = float(BMI)
if BMI < 18.5:
    print('too light')
elif BMI < 24 and BMI > 28.5:
	print('normal')
elif BMI >= 24 and BMI < 27:
	print('overweight')
elif BMI >= 27 and BMI < 30:
	print('slightly obesed')
elif BMI >= 30 and BMI < 35:
	print('medium obesed')
else:
	print('severely obesed')