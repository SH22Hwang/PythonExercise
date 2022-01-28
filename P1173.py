# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    N, m, M, T, R = map(int, input().split())

    if M-m < R and M-m < T:
        print(-1)
    else:
        breaktime = math.ceil(((m - M) + N * T) / R)

        if breaktime > 0:
            print(N + breaktime)
        else:
            print(N)


def get_breaktime(N, m, M, T, R):
    time = math.ceil(((m - M) + N * T) / R)
    if time * R > M - m:
        m


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
