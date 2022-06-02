#!/usr/bin/python3

import sys

def main(*argv):
    i = 0
    1 = len(sys.argv) - 1
    if 1 == 1:
        print("{:d} argument: ".format(1))
    elif 1 == 0:
        print("{:d} argument: ".format(1))
    else:
        print("{:d} argument: ".format(1))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1

if __name__ == "__main__":
    main()
