def P1978():
    n = int(input())
    numbers = list(map(int, input().split()))

    count = 0
    for i in numbers:
        if sieve(i):
            count += 1

    print(count)


def sieve(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False

    return True


if __name__ == '__main__':
    P1978()
