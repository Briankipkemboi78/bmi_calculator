height  = float(input("Enter your height in m: \n"))
weight = int(input("Enter your weight in kgs: \n"))

# BMI is calculated by weight / (height)^2

bmi = round(weight / (height) ** 2, 1)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are Underweight")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your bmi is {bmi}, You are okay!")
else:
    print(f"Your bmi is {bmi}, You are overweight!")