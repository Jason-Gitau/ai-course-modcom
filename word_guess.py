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
        
