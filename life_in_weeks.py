print("Welcome to the Life Left in Weeks until 90 Years Calculator!")

age = input("What is your age in years? \n")

years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left until 90 Years.")