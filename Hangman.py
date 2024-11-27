import random
import HangMan_Words # type: ignore
import HangMan_Art # type: ignore

print("Welcome to HangMan")

lives = 6


chosen_word = random.choice(HangMan_Words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False #Condition
correct_letters = []

while not game_over: #Loop to guess
    guess = input("Guess the letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) # Add correct letters to loop
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You Lose! The word is {chosen_word}")


    if "_" not in display:
        game_over = True
        print("You Win!")

    print(HangMan_Art.Stage[lives])