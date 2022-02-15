import sys

# input = sys.stdin.readline
# s = []
s = set()
lines = int(input())
for _ in range(lines):
    command = list(input().split())
    if command[0] == "add":
        if command[1] not in s:  # 집합의 특성
            s.add(command[1])
    elif command[0] == "remove":
        if command[1] in s:
            s.remove(command[1])
    elif command[0] == "check":
        print(1 if command[1] in s else 0)
    elif command[0] == "toggle":
        if command[1] not in s:
            s.add(command[1])
        else:
            s.remove(command[1])
    elif command[0] == "all":
        s = set([i for i in range(1, 21)])
    elif command[0] == "empty":
        s = set()