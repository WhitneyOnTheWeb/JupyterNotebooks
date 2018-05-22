# Hangman Game
# Example from Invent Your Own Computer Games in Python
# Coded By Whitney King

import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     =====''', '''
  +---+
  O   |
      |
      |
     =====''', '''
  +---+
  O   |
  |   |
      |
     =====''', '''
   +---+
   O   |
  /|   |
       |
      =====''', '''
   +---+
   O   |
  /|\  |
       |
     =====''', '''
   +---+
   O   |
  /|\  |
  /    |
     =====''', '''
   +---+
   O   |
  /|\  |
  / \  |
     =====''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar 
    coyote crow deer dog donkey duck eagle ferret fox frog goat goose 
    hawk lion lizard llama mole monkey moose mouse mule newt otter owl 
    panda parrot pigeon python rabbit ram rat raven rhino salmon seal 
    shark sheep skunk sloth snake spider stork swan tiger toad trout 
    turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    #Returns a random string from the passed list of strings
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:', end= ' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace black with correct letter
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between letters
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player guessed, and validates it
    while True:
        print('Guess a Letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # Returns True  if that player wants to play again
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')



# Begin Gameplay Loop
#------------------------------------------------------------------------------
print('-------------')
print('H A N G M A N')
print('-------------')

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Have player enter a letter 
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is ' + secretWord + '! You\'ve won!')