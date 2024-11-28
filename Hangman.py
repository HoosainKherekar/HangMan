import random
from HangMan_Words import word_list
from HangMan_Art import Stage
from HangMan_Art import Logo 

lives = 6
print(Logo)
chosen_word = random.choice(word_list) #HangMan_Words.word_list imports the files from the module

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False #Condition
correct_letters = []

while not game_over: #Loop to guess

    print(f"******************************{lives}/6 LIVES LEFT******************************")

    guess = input("Guess the letter: ").lower()

    if guess not in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) # Add correct letters to loop
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"******************************YOU LOSE, IT WAS {chosen_word}******************************")


    if "_" not in display:
        game_over = True
        print("You Win!")

    print(Stage[lives]) 