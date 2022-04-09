import sys


def P1620():
    input = sys.stdin.readline
    n1, n2 = map(int, input().split())
    pokemon = {input().strip(): i for i in range(1, n1+1)}  # pokemon dictionary
    keys = list(pokemon.keys())
    test = [input().strip() for _ in range(n2)]  # 테스트 케이스

    for t in test:
        if t.isdigit():
            print(keys[int(t) - 1])
        else:
            print(pokemon[t])


if __name__ == '__main__':
    P1620()
