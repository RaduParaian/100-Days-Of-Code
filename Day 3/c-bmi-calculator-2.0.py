print("Welcome to the Body Mass Index Calculator 2.0!")

height = float(input("What is your height in meters? \n"))
weight = int(input("What is your weight in kilograms? \n"))

bmi = weight / height ** 2

if bmi < 18.5:
  health = "are underweight"
elif bmi < 25:
  health = "have a normal weight"
elif bmi < 30:
  health = "are slightly overweight"
elif bmi < 35:
  health = "are obese"
else:
  health = "are clinically obese"

print(f"Your BMI is {bmi}, you {health}.")