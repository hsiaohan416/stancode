"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    TODO:
    """
    ans = random_word()
    guess = ''
    for i in range(len(ans)):
        guess = guess + '_'
    print('The word is look like ' + guess)
    guess_times = N_TURNS
    print('You have ' + str(guess_times) + ' guesses left.')
    while guess.find('_') != -1:
        input_ch = input('Your guess: ')
        while input_ch.isalpha() == 0 or len(input_ch) > 1:
            print('Illegal format.')
            input_ch = input('Your guess: ')
        input_ch = input_ch.upper()
        if ans.find(input_ch) == -1:
            guess_times = guess_times - 1
            if guess_times < 1:
                print('You are completely hung :(')
                break
            print('There is no ' + input_ch + "'s in the word.")
            print('The word is look like ' + guess)
            print('You have ' + str(guess_times) + ' guesses left.')
        else:
            pupu = ''
            for i in range(len(ans)):
                if input_ch == ans[i]:
                    pupu = pupu + input_ch
                    print('You are corrected!')
                elif guess[i] != '_':
                    pupu = pupu + guess[i]
                else:
                    pupu = pupu + '_'
            guess = pupu
            print('The word is look like ' + guess)
            print('You have ' + str(guess_times) + ' guesses left.')
    if guess.find('_') == -1:
        print('Yor win!!')
    print('The word was: ' + ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
