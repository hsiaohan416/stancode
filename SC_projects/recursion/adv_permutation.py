"""
File: adv_permutation.py
Name: Sharon
------------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking
-- choose, explore, and un-choose
"""


def main():
	permutation([1, 2, 3])


def permutation(lst):
	permutation_helper(lst, [])


def permutation_helper(lst, ans):
	if len(ans) == len(lst):
		print(ans)
	else:
		for num in lst:
			if num not in ans:
				# choose
				ans.append(num)
				# explore
				permutation_helper(lst, ans)
				# un_choose
				ans.pop()







if __name__ == '__main__':
	main()
