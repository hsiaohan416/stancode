"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
EXIT = 1

def main():
    """
    TODO:
    """
    print('This program computes Hailstone sequences. ')
    num_1 = int(input('Enter a number: '))
    steps = 0
    while True:
        if num_1 == EXIT:
            break
        elif num_1 % 2 == 0:
            num_2 = num_1 // 2
            steps = steps + 1
            print(str(num_1) + ' is even, so I take half: ' + str(num_2))
            num_1 = num_2
        else:
            num_2 = num_1 * 3 + 1
            steps = steps + 1
            print(str(num_1) + ' is odd, so I make 3n+1: ' + str(num_2))
            num_1 = num_2
    print('It took ' + str(steps) + ' steps to reach 1. ')







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
