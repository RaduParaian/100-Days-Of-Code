print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? \n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? \n"))
    if age <=12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif age <=18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")
    
    photo_loop = True
    while photo_loop == True:
        wants_photo = input("Do you want a photo taken? Y or N. \n")
        if wants_photo.upper() == "Y":
            bill += 3
            print(f"Your final bill is ${bill}")
            photo_loop = False
        elif wants_photo == "N":
            print(f"Your final bill is ${bill}")
            photo_loop = False
        else: 
            print("Not a valid choice.")
            photo_loop = True

else:
    print("Sorry, you have to grow taller before you can ride.")