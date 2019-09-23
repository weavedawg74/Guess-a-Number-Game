# Guess the Number Game: The computer will think of a secret number from 1 to 20 and ask the user to guess it. After each guess, the computer will tell the user whether the number is too high or too low. The user wins if they can guess the number within six tries.
import random

guessesTaken = 0

print('Hello! What is your name?')
playerName = input()

number = random.randint(1, 20)
print('Well, ' + playerName + ', I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
        
      
