# def P1929():
#     num1, num2 = map(int, input().split())
#
#     prime_numbers = list(i for i in range(num1, num2+1))
#
#     for i in prime_numbers:
#         if sieve(i):
#             print(i)
#
#
# def sieve(num):33
#     if num < 2:
#         return False
#     for i in range(2, int(num**(1/2) + 1)):
#         if num % i == 0:
#             return False
#
#     return True

def P1929():
    num1, num2 = map(int, input().split())
    sieve = [True for _ in range(num2 + 1)]

    for i in range(2, int(num2 ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, num2 + 1, i):
                sieve[j] = False
    if num1 < 2:
        num1 = 2
    for p in range(num1, num2 + 1):
        if sieve[p]:
            print(p)


if __name__ == '__main__':
    P1929()
