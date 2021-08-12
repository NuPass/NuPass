#!/usr/bin/env python
"""
    nupass
    ~~~~~~

    A command-line script for creating user-readible passwords.

    :copyright: (c) 2021 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
import sys
import nupass

def print_usage():
    """Prints out a CLI usage message."""
    print("usage: nupass [number]")
    print("  number: the number of passwords to generate")

def main():
    """Primary entry point for the program."""
    num = 1

    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
        except ValueError:
            print_usage()
            sys.exit(1)

    for i in range(0, num):
        print(nupass.gen_pass())


if __name__ == "__main__":
    main()
