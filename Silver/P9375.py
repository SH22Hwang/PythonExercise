# key0: [value0, value1...]
# key1: [value0, value1...]로 이루어짐.
# key0 = 2^len(values)
# key1 = 2*len(values)
# key0 = len(values)C0 + len(values)C1 = len(values)+1
# key1 = len(values)C0 + len(values)C1 = len(values)+1
# result = key0 * key1 ...
# 모두 아무것도 없는 경우(알몸인 경우, 1)을 빼야함

import sys


def P9375():
    for _ in range(int(input())):
        # 패션왕 신해빈씨의 옷장 정의
        clothes = {}
        for _ in range(int(input())):
            name, c_type = input().rstrip().split()
            if c_type in clothes:
                clothes[c_type] = clothes[c_type] + [name]
            else:
                clothes[c_type] = [name]

        # 신해빈씨의 옷 입는 경우의 수 구하기
        if len(clothes) > 0:
            result = 1
            for k, v in clothes.items():
                result *= len(v) + 1
            print(result - 1)
        else:
            print(0)


if __name__ == '__main__':
    input = sys.stdin.readline
    P9375()