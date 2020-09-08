"""
File: priority_queue_list.py
Name: Sharon
----------------------------------
This program shows how to build a priority queue by
using Python list. We will be discussing 3 different
conditions while appending:
1) Prepend
2) Append
3) Append in between
"""

# This constant controls when to stop the user input
EXIT = '-1'


def main():
    priority_queue = []

    print('--------------------------------')
    while True:
        name = input('Patient (or -1 to quit):')
        if name == EXIT:
            break
        priority = int(input('Priority: '))
        if len(priority_queue) == 0:
            priority_queue.append((name, priority))
        else:
            # Prepend
            if priority_queue[0][1] > priority:
                priority_queue.insert(0, (name, priority))
            # Append
            elif priority_queue[len(priority_queue)-1][1] <= priority:
                priority_queue.append((name, priority))
            # In between
            else:
                for i in range(len(priority_queue)-1):
                    if priority_queue[i][1] <= priority <= priority_queue[i+1][1]:
                        priority_queue.insert(i+1, (name, priority))
                        break

    print('--------------------------------')

    print(priority_queue)


if __name__ == '__main__':
    main()
