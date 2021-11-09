from termcolor import colored
import string

def inputValidate(guess, guessed):
  """Returns the first argument and True if the guess is valid
  and returns a None object and False if it isn't valid"""

  if len(guess) != 1:
    print(colored("Only guess one letter at a time!", "red"))
    return None, False

  if guess not in string.ascii_uppercase:
    print(colored("Only guess letters!", "red"))
    return None, False

  if guess in guessed:
    print(colored("You've already guessed that!", "red"))
    return None, False
  
  return guess, True

def display(hiddenWord, incorrectChars, remainingGuesses):
  """Prints stuff to the screen."""
  print(colored(f"{' '.join(list(hiddenWord))}", "green"))
  print(colored(f"Incorrect letters: {' '.join(incorrectChars)}", "green"))
  print(colored(f"Remaining Guesses: {remainingGuesses}", "green"))