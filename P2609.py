from functools import reduce


def P2609():
    num1, num2 = map(int, input().split())
    max_num = min(num1, num2)  # 약수가 될수 있는 수 중 가장 큰 수
    com_factor = []

    while True:
        i = 0
        for i in range(max_num, 0, -1):
            if i == 1:
                break
            if num1 % i == 0 and num2 % i == 0:
                num1 = int(num1 / i)
                num2 = int(num2 / i)
                max_num = int(min(num1, num2) // 2 + 1)
                com_factor.append(i)
                break

        if i == 1:
            com_factor.append(num1)  # 서로소
            com_factor.append(num2)  # 서로소
            break

    # fold (functional programming)
    def multiply(arr):
        return reduce(lambda x, y: x * y, arr)

    # # Python Style
    # def multiply(arr):
    #     return eval('*'.join([str(n) for n in arr]))

    print(multiply(com_factor[:-2]))
    print(multiply(com_factor))


if __name__ == '__main__':
    P2609()