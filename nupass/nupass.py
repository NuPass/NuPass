#!/usr/bin/env python
"""
    nupass.py
    ~~~~~~~~~

    Generates a user-readible password from
    a wordlist.

    :copyright: (c) 2016 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
import os
import random

FILE_NAME = "wordlist.txt"
#FILE_NAME = "/usr/share/dict/words"
SPEC_CHARS = ['@', '#', '$', '%', '*', '-', "_"]

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
FULL_FILE_NAME = os.path.join(FILE_PATH, FILE_NAME)
TOTAL_BYTES = os.stat(FULL_FILE_NAME).st_size


def get_random_line(file_size):
    """Returns a random line from the wordlist."""
    random_point = random.randint(0, file_size)
    myfile = open(FULL_FILE_NAME)
    myfile.seek(random_point)
    myfile.readline() # required to clear the partial line
    line = myfile.readline()
    myfile.close()

    return line

def get_spec_char():
    """Returns a random special character."""
    return random.choice(SPEC_CHARS)

def gen_pass(min_w_len=5, max_w_len=8):
    """Returns a readible temporary password."""
    word1 = ""
    while len(word1) < min_w_len or len(word1) > max_w_len:
        temp = get_random_line(TOTAL_BYTES)
        word1 = (''.join(j for j in temp if j.isalnum())).capitalize()
    word2 = ""
    while len(word2) < min_w_len or len(word2) > max_w_len:
        temp = get_random_line(TOTAL_BYTES)
        word2 = (''.join(j for j in temp if j.isalnum())).capitalize()
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    return str(num1) + word1 + get_spec_char() + word2 + str(num2)
