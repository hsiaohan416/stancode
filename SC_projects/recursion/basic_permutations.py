"""
File: basic_permutations.py
Name: Sharon
-----------------------------
This program finds all the 3-digits binary permutations
by calling a recursive function binary_permutations.
Students will find a helper function useful in advanced
recursion problems.
"""


def main():
	binary_permutations(5)


def binary_permutations(n):
	permutations_helper(n, '')


def permutations_helper(n, ans):
	if len(ans) == n:
		print(ans)
	else:
		permutations_helper(n, ans+'0')
		permutations_helper(n, ans+'1')


if __name__ == '__main__':
	main()
