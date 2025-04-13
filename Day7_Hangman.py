import random
hangman = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark","baboon","camel"]
chosen_word = word_list[random.randint(0,2)]
placeholder = ""
display = ""
already_guessed = []
game_over = False
lives = 6
count = 0
print(chosen_word)

for word in chosen_word:
    placeholder += "_"
print(placeholder)

while game_over == False:
    guess = input("Enter a letter: \n").lower()
    display = ""
    for word in chosen_word:
        if word == guess:
            display += word
            already_guessed.append(word)
            print(hangman[count] + "\n")
        elif word in already_guessed:
            display += word
            print(hangman[count] + "\n")
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        count += 1
        print(hangman[count])
        if lives == 0:
            game_over = True
            print("U lose, now get outta here u bozo! \n")

    if "_" not in display:
        game_over = True
        print("U win")
    print(display)