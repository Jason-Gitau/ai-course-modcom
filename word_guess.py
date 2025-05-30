import random

# name = input("What is your name? ")

# print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
word=word.lower()
print(word)
length=len(word)

guessed_letter=[] # track letterrs the user has guessed

attempts=1

def display_word_progress():
    display=""
    for char in guessed_letter:
        if char in guessed_letter:
            display+=char + "_"
        else:
            display+="_ "

    return display.split()


print(f"the word has {length} letters {'_ '* length}")

while attempts<7:
    guess=input("Guess a letter ").lower()

    if not guess.isalpha and len(guess) !=1:
        print("Please enter a single alphabetic letter")

    guessed_letter.append(guess)
    if guess in word:
        print(f"Good job. { guess} is in the word")
        print()
        print(display_word_progress())
    
    else:
        attempts-=1
        print(f"sorry, {guess} is not in the word, you have {attempts} attempts remaining")





# changes made to the code by chatgpt

import random

# words to choose from
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# choose a random word
word = random.choice(words)
word = word.lower()
print(f"The word has {len(word)} letters: {'_ ' * len(word)}")

length = len(word)
guessed_letters = []  # track the letters the user has guessed
attempts = 6  # Start with 6 attempts

def display_word_progress():
    display = ""
    for char in word:
        if char in guessed_letters:
            display += char + " "
        else:
            display += "_ "
    return display.strip()

def complete():
    # Check if all letters are guessed correctly
    return all(letter in guessed_letters for letter in word)

# Game loop
while attempts > 0:
    guess = input("Guess a letter: ").lower()

    # Validate input: single letter and alphabetic
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic letter.")
        continue

    if guess in guessed_letters:
        print(f"You have already guessed {guess}.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"Good job! {guess} is in the word.")
        print(display_word_progress())
    else:
        attempts -= 1  # Decrease attempts if guess is wrong
        print(f"Sorry, {guess} is not in the word. You have {attempts} attempts remaining.")
    
    # Check if the user has completed the word
    if complete():
        print(f"Congratulations! You guessed the word: {word}")
        break

# If the player runs out of attempts
if attempts == 0:
    print(f"You lost! The word was: {word}")

        
