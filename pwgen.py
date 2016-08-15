#!/usr/bin/env python
"""
    pwgen.py
    ~~~~~~~~

    Generates a user-readible password from
    a wordlist.

    :copyright: (c) 2016 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
import sys
import os
import random

FILE_NAME = "wordlist.txt"
#FILE_NAME = "/usr/share/dict/words"
SPEC_CHARS = ['@', '#', '$', '%', '*', '-', "_"]
MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 8

def get_random_line(file_size):
    """Returns a random line from the wordlist."""
    random_point = random.randint(0, file_size)
    myfile = open(FILE_NAME)
    myfile.seek(random_point)
    myfile.readline()

    return myfile.readline()

def get_spec_char():
    """Returns a random special character."""
    return random.choice(SPEC_CHARS)

def main():
    """Primary entry point for the program."""
    total_bytes = os.stat(FILE_NAME).st_size
    num = 1

    if len(sys.argv) > 1:
        # TODO: error out if not a number
        num = int(sys.argv[1])

    for i in range(0, num):
        word1 = ""
        while len(word1) < MIN_WORD_LENGTH or len(word1) > MAX_WORD_LENGTH:
            temp = get_random_line(total_bytes)
            word1 = (''.join(j for j in temp if j.isalnum())).capitalize()
        word2 = ""
        while len(word2) < MIN_WORD_LENGTH or len(word2) > MAX_WORD_LENGTH:
            temp = get_random_line(total_bytes)
            word2 = (''.join(j for j in temp if j.isalnum())).capitalize()
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        print str(num1) + word1 + get_spec_char() + word2 + str(num2)


if __name__ == "__main__":
    main()

