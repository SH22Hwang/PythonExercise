# def P1436():
#     list_666 = []
#
#     s = 4
#     salt = 10 ** s
#     shom = '666'
#
#     for i in range(salt):
#         fmt = str(i).zfill(s)
#         list_666.append(int(fmt + shom))
#         list_666.append(int(shom + fmt))
#         for j in range(1, s):
#             list_666.append(int(fmt[:j] + shom + fmt[j:]))
#
#     num = int(input())
#     print(sorted(set(list_666))[num-1])


def P1436():
    list_666 = []

    salt = 10000
    shom = '666'

    for i in range(salt):
        fmt = str(i).zfill(4)

        list_666.append(int(fmt + shom))
        list_666.append(int(fmt[:1] + shom + fmt[1:]))
        list_666.append(int(fmt[:2] + shom + fmt[2:]))
        list_666.append(int(fmt[:3] + shom + fmt[3:]))
        list_666.append(int(shom + fmt))

    print(sorted(set(list_666)))

    num = int(input())
    print(sorted(set(list_666))[num-1])


if __name__ == '__main__':
    P1436()
