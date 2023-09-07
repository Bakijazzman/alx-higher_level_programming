#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    total = 0
    for idx in range(1, length):
        total = total + int(sys.argv[idx])
    print("{}".format(total))
