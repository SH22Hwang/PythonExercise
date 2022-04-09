import sys


def P11723():
    s = [False]*21  # 비트마스킹
    for _ in range(int(input())):
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
            s = [True] * 21
        elif command[0] == "empty":
            s = [False] * 21


if __name__ == '__main__':
    input = sys.stdin.readline
    P11723()
