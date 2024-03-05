import random
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_score = 0
computer_score = 0

play_loop = True
while play_loop == True:

    leaderboard = f"You: {user_score}, Computer: {computer_score}"

    user_loop = True
    while user_loop == True:
        user_choice = input("What do you choose? r, p, or s. \n").lower()
        if user_choice == "r":
            user_choice = 0
            user_loop = False
        elif user_choice == "p":
            user_choice = 1
            user_loop = False
        elif user_choice == "s":
            user_choice = 2
            user_loop = False
        else:
            user_loop = True
            print("Not a valid choice")
    
    print(game_images[user_choice])
    time.sleep(1)

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    time.sleep(1)

    if user_choice == 0 and computer_choice == 2:
        user_score +=  1
        print("You win!")
        time.sleep(0.5)
        print(leaderboard)
    elif computer_choice == 0 and user_choice == 2:
        computer_score += 1
        print("You lose")
        time.sleep(0.5)
        print(leaderboard)
    elif computer_choice > user_choice:
        computer_score += 1
        print("You lose")
        time.sleep(0.5)
        print(leaderboard)
    elif user_choice > computer_choice:
        user_score +=  1
        print("You win!")
        time.sleep(0.5)
        print(leaderboard)
    elif computer_choice == user_choice:
        print("It's a draw")
        time.sleep(0.5)
        print(leaderboard)

    time.sleep(1)

    play_again_loop = True
    while play_again_loop == True:
        again_choice = input("Play again? y, or n. \n").lower()
        if again_choice == "y":
            play_loop = True
            play_again_loop = False
        elif again_choice == "n":
            play_loop = False
            play_again_loop = False
            
            time.sleep(1)
        else:
            play_again_loop = True
            print("Not a valid choice.")
