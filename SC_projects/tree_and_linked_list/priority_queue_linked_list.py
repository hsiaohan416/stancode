"""
File: priority_queue.py
Name: Sharon
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It controls the condition to break the input loop
EXIT = '-1'


class LinkedList:
	def __init__(self, value, next):
		self.value = value
		self.next = next


def main():
	linked_list = LinkedList(None, None)
	while True:
		name = input(f'Name of patient ({EXIT} to quit): ')
		if name == EXIT:
			break
		priority = int(input('Priority: '))
		if linked_list.value is None:
			linked_list.value = (name, priority)
		else:
			if linked_list.value[1] > priority:
				# New node at the beginning
				data = LinkedList((name, priority), linked_list)
				linked_list = data
			else:
				# New node in between
				temp = linked_list
				while temp.next is not None:
					if temp.value[1] <= priority <= temp.next.value[1]:
						data = LinkedList((name,priority), temp.next)
						temp.next = data
						break
					temp = temp.next
				# New node at the end
				if temp.next is None:
					temp.next = LinkedList((name, priority), None)
	traversal(linked_list)


def traversal(linked_list):
	temp = linked_list
	while temp.next is not None:
		print(temp.value)
		temp = temp.next
	print(temp.value)


if __name__ == '__main__':
	main()
