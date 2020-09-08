"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 3


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()



def head():
	for i in range(SIZE):
		print(' ', end="")
		for j in range(2*SIZE):
			if i+j < SIZE-1:
				print(' ', end="")
			else:
				if j < SIZE:
					print('/', end="")
				elif j > SIZE:
					if j - i > SIZE + 1:
						print(' ', end="")
					else:
						print('\\', end="")
					if j == 2*SIZE-1:
						if j == (2 * i) + 1:
							print('\\', end="")
			if SIZE == 1:
				if j == 0:
					print('\\', end="")
		print('')


def belt():
	print('+', end="")
	for i in range(2*SIZE):
		print('=', end="")
	print('+')


def upper():
	for i in range(SIZE):
		print('|', end="")
		for j in range(2 * SIZE):
			if i+j < SIZE-1:
				print('.', end="")
			elif j-i > SIZE:
				print('.', end="")

			elif (i+j) % 2 == 0:
				if SIZE % 2 == 1:
					print('/', end="")
				else:
					print('\\', end="")
			elif (i+j) % 2 == 1:
				if SIZE % 2 == 1:
					print('\\', end="")
				else:
					print('/', end="")
		print('|')


def lower():
	for i in range(SIZE):
		print('|', end="")
		for j in range(2 * SIZE):
			if j-i < 0:
				print('.', end="")
			elif i+j > 2*SIZE-1:
				print('.', end="")
			elif (i+j) % 2 == 0:
					print('\\', end="")
			elif (i+j) % 2 == 1:
					print('/', end="")
		print('|')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()