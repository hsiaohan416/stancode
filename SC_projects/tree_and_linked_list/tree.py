"""
File: tree.py
Name: Sharon
-------------------------
This file shows the basic concepts for binary trees.
After constructing a tree, we will do 3 traversal examples:
Pre-order
In-order 
Post-order
"""


class Tree:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right


def main():
	root = Tree(17, None, None)

	leaf1= Tree(2, None, None)
	leaf2 = Tree(6, None, None)
	leaf3 = Tree(18, None, None)
	leaf4 = Tree(40, None, None)

	node1 = Tree(4, leaf1, leaf2)
	node2 = Tree(19, leaf3, leaf4)

	root.left = node1
	root.right = node2

	pre_order(root)
	in_order(root)
	post_order(root)


def pre_order(root):
	if root is None:
		pass
	else:
		print(root.value)
		pre_order(root.left)
		pre_order(root.right)


def in_order(root):
	if root is None:
		pass
	else:
		in_order(root.left)
		print(root.value)
		in_order(root.right)


def post_order(root):
	if root is None:
		pass
	else:
		post_order(root.left)
		post_order(root.right)
		print(root.value)


if __name__ == '__main__':
	main()
