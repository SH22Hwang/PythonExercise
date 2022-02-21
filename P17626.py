from itertools import combinations
import time


# 시간 초과
def P17626():
    num = int(input())
    s = time.time()
    if int(num ** 0.5) == num ** 0.5:
        print(1)
        exit(0)

    squares = list(x ** 2 for x in range(1, int(num ** 0.5)+1))
    for i in range(2, 5):
        for case in combinations(squares, i):
            if sum(case) == num:
                print(case)
                print(i)
                print(time.time() - s)
                exit(0)


if __name__ == '__main__':
    P17626()
