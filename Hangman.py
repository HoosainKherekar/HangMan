import random

print("Welcome to HangMan")

Stage = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = [
    "ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", 
    "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", 
    "frog", "goat", "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose", 
    "mouse", "mule", "newt", "otter", "owl", "panda", "parrot", "pigeon", "python", "rabbit", 
    "ram", "rat", "raven", "rhino", "salmon", "seal", "shark", "sheep", "skunk", "sloth", 
    "snake", "spider", "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle", 
    "weasel", "whale", "wolf", "wombat", "zebra"]

lives = 6


chosen_word = random.choice(word_list)

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
            print("You Lose!")

    print(Stage[lives])

    if "_" not in display:
        game_over = True
        print("You Win!")