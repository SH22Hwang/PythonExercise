import sys

while True:
    a = sum(map(int, sys.stdin.readline().split()))
    if a > 0:
        print(a)
    else:
        break
