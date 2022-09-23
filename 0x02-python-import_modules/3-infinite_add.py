#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    check = 0
    count = len(argv)
    if count == 1:
        print("{:d}".format(count - 1))
    else:
        for i in range(1, count):
            check += int(argv[i])
        print("{:d}".format(check))
