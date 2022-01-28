import sys
import time


def P1225():
    lines = int(input())

    start = time.time()
    # numbers = sorted((int(input()) for x in range(lines)))
    numbers = sorted((int(sys.stdin.readline()) for _ in range(lines)))

    print(*numbers, sep='\n')

    end = time.time()
    print(f"{end - start:.5f} sec")


if __name__ == '__main__':
    P1225()

