"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    """

    strand = input("Please give me a DNA strand and I'll find the complement: ")
    strand = strand.upper()
    new_dna = complement(strand)
    print(new_dna)


def complement(strand):
    dna = ""
    for base in strand:
        if base == "A":
            dna = dna + "T"
        elif base == "T":
            dna = dna + "A"
        elif base == "C":
            dna = dna + "G"
        elif base == "G":
            dna = dna + "C"
        else:
            dna = dna + "*"
    return dna






###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
