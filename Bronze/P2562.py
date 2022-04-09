def P2562():
    nums = [int(input()) for _ in range(9)]

    temp, position = 0, 0
    for i in nums:
        if temp < i:
            temp = i
            position = nums.index(i) + 1

    print(temp)
    print(position)


if __name__ == '__main__':
    P2562()
