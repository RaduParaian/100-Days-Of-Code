print("Welcome to the Body Mass Index Calculator!")

height = float(input("What is your height in meters? \n"))
weight = int(input("What is your weight in kilograms? \n"))

bmi = weight / height ** 2

bmi_as_int = int(bmi)
print(f"Your BMI is {bmi_as_int}!")