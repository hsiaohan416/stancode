"""
File: dice_rolls_sum.py
Name: Sharon
-----------------------------
This program finds all the dice rolls permutations
that sum up to a constant TOTAL. Students will find
early stopping a good strategy of decreasing the number
of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8

# global variable
run_times = 0


def main():
    dice_sum(TOTAL)
    print(f'Total run times: {run_times}')


def dice_sum(total):
    dice_sum_helper(total, [])


def dice_sum_helper(total, ans):
    global run_times
    run_times += 1
    if sum(ans) == total:
        print(ans)

    else:
        for roll in [1, 2, 3, 4, 5, 6]:
            if sum(ans) <= total:
                diff = total - sum(ans)
                if diff > roll:
                    # choose
                    ans.append(roll)
                    # explore
                    dice_sum_helper(total, ans)
                    # un-choose
                    ans.pop()


if __name__ == '__main__':
    main()
