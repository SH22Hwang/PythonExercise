def P4673():
    temp = [dn(x) for x in range(1, 10000)]
    selfNumber = [x for x in range(1, 10000) if x not in temp]
    print(*selfNumber, sep='\n')


def dn(n):
    # n을 문자열로 바꿔서 각 자리별로 가져와 int로 저장하고 n + 각 자리의 합 반환
    return n + sum([int(i) for i in str(n)])


if __name__ == '__main__':
    P4673()
