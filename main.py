import functions, wordsList, random
from termcolor import colored

#Yay variables
targetWord = random.choice(wordsList.words)
hiddenWord = ''.join(['_' for i in range(len(targetWord))])
remainingGuesses = 12
guessedChars = []
incorrectChars = []

# -- Main Game Loop --
while True:

  #Display text HUD
  functions.display(hiddenWord, incorrectChars, remainingGuesses)
  
  #Handle guess and get its validity
  guess = input(colored("Guess a letter:", 'green')).upper()
  guess, valid = functions.inputValidate(guess, guessedChars)
  
  #Restart loop if guess was invalid
  if not valid:
    continue

  #Store the guessed letter
  guessedChars.append(guess)
  guessedChars = sorted(guessedChars)

  #Now we save the guess into hiddenWord if applicable
  if guess in targetWord:

    #Increment remainingGuesses so you only lose guesses on an incorrect guess
    remainingGuesses += 1

    #Find the correct letters and update the corresponding spot in hiddenWord 
    for i in range(len(targetWord)):
      if guess == targetWord[i]:
        #StRiNgS aRe ImMuTaBlE oBjEcTs
        hiddenWord = list(hiddenWord)
        hiddenWord[i] = guess
        hiddenWord = ''.join(hiddenWord)

  #Or we save the guess into incorrect guesses
  else:
    incorrectChars.append(guess)
    incorrectChars = sorted(incorrectChars)

  #If the player has won exit the main loop
  if hiddenWord == targetWord:
    won = True
    break

  #Decrement remainingGuesses then exit the loop if the player has run out
  remainingGuesses -= 1
  if remainingGuesses <= 0:
    won = False
    break

#Funky final text yay
if won:
  text = "Congratulations! You Won!"
  color, back = "yellow", "on_green"

else:
  text = f"Sorry, you lost. The word was: {targetWord}"
  color, back = "red", "on_yellow"

line = ''.join([" " for i in text])
print(colored(line, color, back))
print(colored(text, color))
print(colored(line, color, back))