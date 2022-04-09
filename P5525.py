import sys


def P5525():
    n = int(input())
    pn = 'I' + 'OI' * n
    # pn = 'I' + 'OI' * int(input())
    length = int(input())
    string = input().strip()

    sum, x = 0, 0
    while x < length:
        # temp = string[x:x+len(pn)]
        # if pn in temp:
        if pn in string[x:]:
            x += 1
            sum += 1
        x += 1

    print(sum)


if __name__ == '__main__':
    input = sys.stdin.readline
    P5525()
