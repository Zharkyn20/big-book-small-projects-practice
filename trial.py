import random

NUM_DIGITS = 3
MAX_DIGIT_NUMS = 10

def main():
    print('''Bagels a deductive logic game.
    By Al Sweigart al@inventwithpython.com

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
      Pico          One digit is correct but in the wrong position.
      Fermi         One digit is correct and in the right position.
      Bagels        No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
     clues would be Fermi Pico'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(NUM_DIGITS))

        numGuesses = 1

        while numGuesses <= MAX_DIGIT_NUMS:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}'.format(numGuesses))
                guess = input('> ')

        numGuesses += 1

def getSecretNum():
    digits = list('0123456789')
    random.shuffle(digits)
    secretNum = ''

    for i in range(NUM_DIGITS):
        secretNum += str(digits[i])

    return secretNum


    return secretNum