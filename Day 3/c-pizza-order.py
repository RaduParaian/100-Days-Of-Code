print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size.capitalize() == "S":
  bill = 15
elif size.capitalize() == "M":
  bill = 20
elif size.capitalize() == "L":
  bill = 20
else:
  print("Not a valid choice.")

if add_pepperoni.capitalize() == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")