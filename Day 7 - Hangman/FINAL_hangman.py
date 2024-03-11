import random
import FINAL_hangman_art
import FINAL_hangman_words
from FINAL_hangman_art import logo, stages
from FINAL_hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

print(logo + "\n")

display = []
for _ in chosen_word:
    display += "_"
print(f"Word: {' '.join(display)}\n")

word_length = len(chosen_word)

end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life. \n")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.\n")
            print(f"The word was {chosen_word}")

    print(f"Word: {' '.join(display)}\n")

    if "_" not in display:
        end_game = True
        print("You win.\n")

    print(stages[lives])