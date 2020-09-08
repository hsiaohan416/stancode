"""
File: boggle.py
Name: Sharon Tseng
----------------------------------------
This program recursively finds all the word(s) in a 4 * 4 world
that can line-up with their neighbors, and the length of the
word will be longer or equals to 4 characters. The 4 * 4 world
is input by 4 rows by user, and all the characters input should
be separated by blanks.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# Global variable
dict_list = []                # A list of all the words in the dictionary
letter_lst = []               # A list of all the character input
word_num = 0                  # Number of the words found


def main():
	global letter_lst
	read_dictionary()
	# Enter the data
	for i in range(4):
		row = input(f'{i+1} row of letters:').lower().split()
		if len(row) == 4:
			check = check_input(row)
			if check is False:
				print('Illegal input')
				break
			else:
				letter_lst += row
		else:
			print('Illegal input')
			break
		if i == 3:
			# Distinguish the same character in the list
			for j in range(len(letter_lst)):
				letter2 = letter_lst[:j] + letter_lst[(j+1):]
				if letter_lst[j] in letter2:
					letter_lst[j] = letter_lst[j].upper()

			# choose
			for k in range(len(letter_lst)):
				ans = letter_lst[k]
				find_boggle(k, ans, [])
			print(f'There are {word_num} words in total.')


def check_input(row):
	# This function checks each character input
	for i in range(len(row)):
		if len(row[i]) > 1 or row[i].isalpha() is False:
			return False


def find_boggle(k, ans, ans_lst):
	global word_num
	# Base case: When the length of ans is longer or equals to 4
	if len(ans) >= 4:
		boggle_2(k, ans, ans_lst)        # Check the word longer than 4 characters
		ans = ans.lower()
		if ans in dict_list and ans not in ans_lst:
			print(f'Found: {ans}')
			ans_lst.append(ans)
			word_num += 1
	# Recursion
	else:
		boggle_2(k, ans, ans_lst)


def boggle_2(k, ans, ans_lst):
	# the index of the chosen character's neighbor
	neighbor = [k - 5, k - 4, k - 3, k - 1, k + 1, k + 3, k + 4, k + 5]
	# choose
	for i in neighbor:
		if i < 0 or i > 15:
			pass
		elif k % 4 == 0 and i % 4 == 3:
			pass
		elif k % 4 == 3 and i % 4 == 0:
			pass
		else:
			if letter_lst[i] not in ans:
				k = i                      # Assign the position of the new last character.
				ans += letter_lst[k]
				check = has_prefix(ans.lower())
				if check is True:
					# explore
					find_boggle(k, ans, ans_lst)
				# un-choose
				ans = ans[:len(ans) - 1]
				# If one character is removed, re-index the last character.
				for num in range(len(letter_lst)):
					if letter_lst[num] == ans[len(ans) - 1]:
						k = num
						break


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


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	in_list = 0
	for vocab in dict_list:
		if vocab[:len(sub_s)] == sub_s:
			in_list += 1
			return True
	if in_list == 0:
		return False


if __name__ == '__main__':
	main()
