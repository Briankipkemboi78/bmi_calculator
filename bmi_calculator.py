height  = float(input("Enter your height in m: \n"))
weight = int(input("Enter your weight in kgs: \n"))

# BMI is calculated by weight / (height)^2

bmi = round(weight / (height) ** 2, 2)

print(f"Your bmi is {bmi}")