import sys


def P17129():
    n1, n2 = map(int, input().split())

    # 사이트의 주소와 비밀번호 입력
    # sites = {}
    # for _ in range(n1):
    #     s, p = input().split()
    #     sites[s] = p

    sites = dict(input().split() for _ in range(n1))

    # for _ in range(n2):
    #     print(sites[input().strip()])
    print(*list(sites[input().strip()] for _ in range(n2)), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    P17129()