"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	TODO:
	"""
	print('hsiao quadratic solver!')
	a = int(input('Enter a= '))
	if a == 0:
		print('FUCK YOU!! Enter again!!')
		a = int(input('Enter a= '))
	b = int(input('Enter b= '))
	c = int(input('Enter c= '))
	discriminant = b*b-4*a*c
	if discriminant > 0:
		root_1 = (-b+math.sqrt(discriminant))/2*a
		root_2 = (-b-math.sqrt(discriminant))/2*a
		print("Two Roots=" + str(root_1) + "," + str(root_2))
	elif discriminant == 0:
		root_0 = -b/2*a
		print('One Root= ' + str(root_0))
	else:
		print('No Real Roots! Ugly Guy!')








###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
