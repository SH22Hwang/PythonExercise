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

# def P11723():
#     input = sys.stdin.readline
#     # s = []
#     s = set()
#     lines = int(input())
#     cmds = list(list(input().split()) for _ in range(lines))
#     for command in cmds:
#         if command[0] == "add":
#             if command[1] not in s:  # 집합의 특성
#                 s.add(command[1])
#         elif command[0] == "remove":
#             if command[1] in s:
#                 s.remove(command[1])
#         elif command[0] == "check":
#             print(1 if command[1] in s else 0)
#         elif command[0] == "toggle":
#             if command[1] in s:
#                 s.add(command[1])
#             else:
#                 s.remove(command[1])
#         elif command[0] == "all":
#             s = set([i for i in range(1, 21)])
#         elif command[0] == "empty":
#             s = set()

def P11723():
    input = sys.stdin.readline
    s = [False for _ in range(21)]  # 비트마스킹

    lines = int(input())
    for _ in range(lines):
        command = list(input().strip().split())  # strip() 추가(개행문자 제거)
        if len(command) == 2:
            command[1] = int(command[1])

        if command[0] == "add":
            if not s[command[1]]:  # x가 이미 있는 경우에는 연산을 무시. False일 때만 실행
                s[command[1]] = True
        elif command[0] == "remove":
            if s[command[1]]:
                s[command[1]] = False
        elif command[0] == "check":
            print(1 if s[command[1]] else 0)
        elif command[0] == "toggle":
            if s[command[1]]:
                s[command[1]] = False
            else:
                s[command[1]] = True
        elif command[0] == "all":
            s = [True for _ in range(21)]
        elif command[0] == "empty":
            s = [False for _ in range(21)]


if __name__ == '__main__':
    P11723()
