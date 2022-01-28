# def P1181():
#     num = int(input())  # 단어의 개수 N
#     words = list(input() for _ in range(num))  # 단어의 개수만큼 리스트에 추가
#     words = [word for word in sorted(words, key=lambda item: len(item))]
#     print(*words, sep='\n')  # 딕셔너리의 값을 한 줄씩 출력


def P1181():
    num = int(input())  # 단어의 개수 N
    words = list(input() for _ in range(num))  # 단어의 개수만큼 리스트에 추가

    words_dict = {word: len(word) for word in sorted(sorted(words), key=lambda item: len(item))}

    print(*words_dict.keys(), sep='\n')  # 딕셔너리의 값을 한 줄씩 출력


if __name__ == '__main__':
    P1181()
