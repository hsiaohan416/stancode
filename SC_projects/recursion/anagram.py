"""
File: anagram.py
Name: Sharon Tseng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 21

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
dict_list = []                # A list of all the words in the dictionary
ans_lst = []                  # A list of all the words found
anagram_num = 0               # Number of the anagram found


def main():
    global anagram_num, ans_lst
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    read_dictionary()
    while True:
        word = input('Find anagrams for: ').lower()       # Case insensitive
        # Distinguish the same character in one word (make the first one into upper case)
        for i in range(len(word)):
            word_2 = word[:i] + word[(i + 1):]            # all character without word[i]
            if word_2.find(word[i]) != -1:
                word = word[:i] + word[i].upper() + word[(i + 1):]

        if word == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(word)
            print(f'{anagram_num} anagrams: {ans_lst}')
            anagram_num = 0
            ans_lst = []


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global dict_list
    with open(FILE, 'r') as f:
        for line in f:
            vocab = line.split()
            dict_list += vocab


def find_anagrams(s):
    """
    :param s: (str) The word wants to find anagram
    :return: this function returns nothing
    """
    find_helper(s, '')


def find_helper(s, ans):
    global anagram_num
    # Base case: When the length of the answer equals to the length of word input.
    if len(ans) == len(s):
        ans = ans.lower()
        if ans in dict_list and ans not in ans_lst:
            print(f'Found: {ans}')
            ans_lst.append(ans)
            anagram_num += 1
            print('Searching...')
    # Recursion
    else:
        for i in range(len(s)):
            if s[i] not in ans:
                # choose
                ans += s[i]
                ans_check = ans.lower()
                check = has_prefix(ans_check)
                if check is True:
                    # explore
                    find_helper(s, ans)
                # un-choose
                ans = ans[:len(ans)-1]


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by the given characters
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    n = len(sub_s)
    in_list = 0
    for vocab in dict_list:
        if vocab[:n] == sub_s:
            in_list += 1
            return True
    if in_list == 0:
        return False


if __name__ == '__main__':
    main()
