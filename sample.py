weight = input("What is your weight in Kgs? ")
height = input("What is your height in m? ")

w = float(weight)
h = float(height)
bmi = w/h**2  # 10*83 math.pow(h,2) h*h

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are healthy")
elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("You are obese 1")
elif bmi >= 35 and bmi <= 39.9:
    print("You are obese 2")
else:
    print("You are obese 3")
