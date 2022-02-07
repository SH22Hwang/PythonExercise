# 스택 구현하기
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 파이썬 리스트의 기본 메소드 push, pop을 이용하지 않고 구현

class MyStack:
    stack = []
    
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)
        # print 또는 return 없음
    def pop(self):
        temp = self.top()
        if temp == -1:
            return -1
        else:
            del self.stack[-1]
            return temp

    def size(self):
        return len(self.stack)

    def empty(self):
        return 0 if self.size() > 0 else 1

    def top(self):
        return -1 if self.empty() else self.stack[-1]


def P10828():
    stk = MyStack()
    lines = int(input())
    cmd = list(list(input().split()) for _ in range(lines))
    # print(cmd)
    for i in range(lines):
        if cmd[i][0] == 'push':
            stk.push(cmd[i][1])
        elif cmd[i][0] == 'pop':
            print(stk.pop())
        elif cmd[i][0] == 'size':
            print(stk.size())
        elif cmd[i][0] == 'empty':
            print(stk.empty())
        elif cmd[i][0] == 'top':
            print(stk.top())


if __name__ == '__main__':
    P10828()
