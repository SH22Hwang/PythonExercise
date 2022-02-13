def P9012():
    num = int(input())
    vps = list(input() for _ in range(num))
    stack = []

    for string in vps:
        try:
            for char in string:
                if char == '(':
                    stack.append(1)
                elif char == ')':
                    stack.pop()

        except IndexError:
            print('NO')
            continue

        print('NO' if stack else 'YES')
        stack.clear()


if __name__ == '__main__':
    P9012()
