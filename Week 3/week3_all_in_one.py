# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import string
import random

WORDLIST_FILENAME = "words.txt"



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
      >>> secretWord = 'apple' 
      >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
      >>> print(isWordGuessed(secretWord, lettersGuessed))
      False
    '''
    # FILL IN YOUR CODE HERE...
    output=False
    counter=len(secretWord)
    for let in secretWord:
        if let in lettersGuessed:
            counter-=1
            if counter==0:
                output=True
                break
    return output
    
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      >>> secretWord = 'apple' 
      >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
      >>> print(getGuessedWord(secretWord, lettersGuessed))
      '_ pp_ e'
    '''
    # FILL IN YOUR CODE HERE...
    
    output=""
    for let in secretWord:
        if let in lettersGuessed:
            output+=let
        else:
            output+=" _ "
    return output
    

     
    
        
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
      lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
      >>> print(getAvailableLetters(lettersGuessed))
      abcdfghjlmnoqtuvwxyz
    '''
    # FILL IN YOUR CODE HERE...
    output=""
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            output+=i
    return output

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses=[]
    print('Welcome to the game Hangman!')
    lenght=len(secretWord)
    print('I am thinking of a word that is ' +str(lenght)+' letters long')
    
    counter=8
    
    
    print('-------------')
    while counter>0:
        print('You have '+str(counter)+' guesses left')
        print('Available letters :'+getAvailableLetters(guesses))
        guess=input('Please guess a letter: ')
               
        if guess in guesses:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, guesses))
        
        elif guess in secretWord:
            guesses.append(guess)
            print('Good guess: '+getGuessedWord(secretWord, guesses))
        else:
            counter-=1
            guesses.append(guess)
            print('Oops! That letter is not in my word: '+getGuessedWord(secretWord, guesses))
        
        if isWordGuessed(secretWord,guesses):
            print('-------------')
            break
        print('-------------')
        
   
    if not isWordGuessed(secretWord,guesses):
            print('Sorry, you ran out of guesses. The word was '+secretWord)
    else:
        print('Congratulations, you won!')
            
        







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)