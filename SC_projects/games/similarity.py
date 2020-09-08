"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    """
    long_sequence = input('Please give me a DNA sequence to start:')
    long_sequence = long_sequence.upper()
    short_sequence = input('What sequence do you want to match?')
    short_sequence = short_sequence.upper()
    match_ans = match(short_sequence, long_sequence)
    print('The best match is '+match_ans)


def match(short_sequence, long_sequence):
    similar = 0
    max_similar = 0
    best_sequence = ""
    for i in range(len(long_sequence)-len(short_sequence)+1):
        selected = long_sequence[0+i:len(short_sequence)+i]
        for j in range(len(short_sequence)):
            if short_sequence[j] == selected[j]:
                similar = similar + 1
        similarity = (similar / len(short_sequence)) * 100
        if similarity > max_similar:
            max_similar = similarity
            best_sequence = selected
    return best_sequence







###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
