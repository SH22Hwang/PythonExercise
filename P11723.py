import sys


# class Set:
#     def __init__(self):
#         self.S = []
#
#     def add(self, x):
#         self.S.append(x)
#
#     def remove(self, x):
#         if x in self.S:
#             self.S.remove(x)
#
#     def check(self, x):
#         if x in self.S:
#             print(1)
#         else:
#             print(0)
#
#     def toggle(self, x):
#         if x in self.S:
#             self.S.remove(x)
#         else:
#             self.S.append(x)
#
#     def all(self):
#         self.S = [i for i in range(1, 21)]
#
#     def empty(self):
#         self.S.clear()


def P11723():
    input = sys.stdin.readline
    # s = []
    s = set()
    lines = int(input())
    cmds = list(list(input().split()) for _ in range(lines))
    for command in cmds:
        if command[0] == "add":
            if command[1] not in s:  # 집합의 특성
                s.add(command[1])
        elif command[0] == "remove":
            if command[1] in s:
                s.remove(command[1])
        elif command[0] == "check":
            print(1 if command[1] in s else 0)
        elif command[0] == "toggle":
            if command[1] in s:
                s.add(command[1])
            else:
                s.remove(command[1])
        elif command[0] == "all":
            s = set([i for i in range(1, 21)])
        elif command[0] == "empty":
            s = set()


if __name__ == '__main__':
    P11723()
