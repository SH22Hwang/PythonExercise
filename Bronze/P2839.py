def main():
    num = int(input())
    recursive = int(num / 3) + 1

    for i in range(recursive):
        if num % 5 == 0:
            print(int(num / 5 + i))
            break
        else:
            num -= 3

    if num < 5 and num != 0:
        print(-1)


if __name__ == '__main__':
    main()
