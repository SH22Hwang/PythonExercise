from itertools import product


# # 4개 이하의 자연수의 제곱
# def combinations(array, r):
#     for i in range(len(array)):
#         if r == 1:
#             yield [array[i]]
#         else:
#             ## array[i+1: ] -> array[i: ] 변경
#             for next in combinations(array[i:], r-1):
#                 yield [array[i]] + next


def P17626():
    num = int(input())
    if int(num ** 0.5) == num ** 0.5:
        print(1)
        exit(0)

    squares = list(map(lambda x: x ** 2, range(1, int(num ** 0.5) + 1)))
    for i in range(2, 5):
        for case in product(squares, repeat=i):
            if sum(case) == num:
                print(i)
                exit(0)


if __name__ == '__main__':
    P17626()
