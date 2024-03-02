print("Welcome to the Body Mass Index Calculator.")

height = input("What is your height in meters? \n")
weight = input("What is your weight in kilograms? \n")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(f"Your BMI is {bmi_as_int}!")