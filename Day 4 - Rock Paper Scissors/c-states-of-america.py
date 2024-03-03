print("Welcome to the States of America Checker, we will check the order of the states joining the union and give you your chosen place!")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
"New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", 
"Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
"California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
"Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

chosen_place = int(input("Choose a place out of 50. \n"))

chosen_place_minus = chosen_place - 1

if chosen_place == 1:
    print(states_of_america[chosen_place_minus] + " joined USA " + str(chosen_place) + "st")
elif chosen_place == 2:
    print(states_of_america[chosen_place_minus] + " joined USA " + str(chosen_place) + "nd")
elif chosen_place == 3:
    print(states_of_america[chosen_place_minus] + " joined USA " + str(chosen_place) + "rd")
elif chosen_place > 50:
    print("Not a valid state.")
else:
    print(states_of_america[chosen_place_minus] + " joined USA " + str(chosen_place) + "th")