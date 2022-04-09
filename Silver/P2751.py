def P2751():
    str1, str2 = map(list, input().split())
    str1 = list(map(int, str1))
    str2 = list(map(int, str2))

    # sumList = list(map(lambda x: list(map(lambda y: x * y, str2)), str1))

    print(sum(str1) * sum(str2))


if __name__ == '__main__':
    P2751()
