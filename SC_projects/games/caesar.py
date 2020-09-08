"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:
    """
    move = int(input('Secret number: '))
    old_string = input("What's the ciphered string? ")
    old_string = old_string.upper()
    new_string = decipher(move, old_string)
    # print('The deciphered string number is: '+new_string)
    print(new_string)


def decipher(move, old_string):
    ans = ''
    new_alphabet = ALPHABET[26-move:26]+ALPHABET[:26-move]
    for ch in old_string:
        num = int(new_alphabet.find(ch))
        if num == -1:
            ans = ans + ch
        else:
            ans = ans + ALPHABET[num]
    return ans






#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
