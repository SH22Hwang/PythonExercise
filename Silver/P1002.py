import sys


def P1002():
    for _ in range(int(input())):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        rp = r1 + r2
        rm = abs(r1 - r2)
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        if distance == 0 and r1 == r2:  # ok
            print(-1)
        elif rp < distance or distance < rm:
            print(0)
        elif distance == rp or distance == rm:  # ok
            print(1)
        elif rm < distance < rp:  # ok
            print(2)


if __name__ == '__main__':
    input = sys.stdin.readline
    P1002()