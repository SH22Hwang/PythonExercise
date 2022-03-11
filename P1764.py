import sys


def P1764():
    n1, n2 = map(int, input().split())
    people = set(input() for _ in range(n1))

    names = []
    for _ in range(n2):
        temp = input()
        if temp in people:
            names.append(temp.strip())

    print(len(names))
    print(*sorted(names), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    P1764()