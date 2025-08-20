import random

    
stages = [
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
    '''
]

word_list = ["games", "anime", "mango"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False

correct_letters = []

while not game_over:

    print(f"You have {lives}/6 lives left")

    guess = input("Guess a letter: \n").lower()
     
    if guess in correct_letters:
        print(f"you already guessed {guess}")

    # TODO-2: Create a "display" that puts the guess letter in the right positions and _ if not
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)


    if guess  not in chosen_word:
        lives -= 1
        print("wrong letter chosen")
        if lives == 0:
            game_over = True
            print(f"it was {chosen_word} you lose 😔")

    if ("_") not in display:
            game_over = True
            print(f"it was {chosen_word} you win!")

    print(stages[lives])
