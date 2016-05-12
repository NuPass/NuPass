#!/usr/bin/env python
import sys
import os
import random

total_bytes = 0
file_name = "/usr/share/dict/words"
spec_chars = ['@', '#', '$', '%', '*', '-', "_"]
MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 8

def get_random_line():
    random_point = random.randint(0, total_bytes)
    file = open(file_name)
    file.seek(random_point)
    file.readline()

    return file.readline()

def init_file():
    global total_bytes
    total_bytes = os.stat(file_name).st_size

def get_spec_char():
    return random.choice(spec_chars)

def main():
    init_file()
    num = 1

    if len(sys.argv) > 1:
        # TODO: error out if not a number
        num = int(sys.argv[1])

    for i in range(0, num):
        word1 = ""
        while len(word1) < MIN_WORD_LENGTH or len(word1) > MAX_WORD_LENGTH:
            temp = get_random_line()
            word1 = (''.join(j for j in temp if j.isalnum())).capitalize()
        word2 = ""
        while len(word2) < MIN_WORD_LENGTH or len(word2) > MAX_WORD_LENGTH:
            temp = get_random_line()
            word2 = (''.join(j for j in temp if j.isalnum())).capitalize()
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        print str(num1) + word1 + get_spec_char() + word2 + str(num2)


if __name__ == "__main__":
    main()