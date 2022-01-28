from collections import Counter


def P1157():
    word = list(input().upper())
    count_char = Counter(word).most_common(2)
    if len(word) > 1 and count_char[0][1] == count_char[1][1]:
        print("?")
    else:
        print(count_char[0][0])


if __name__ == '__main__':
    P1157()
