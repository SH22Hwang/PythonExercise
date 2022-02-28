scale = list(map(int, input().split()))

flag = True
if scale[0] == 1:
    for i in range(1, 9):
        if i != scale[i-1]:
            flag = False
            break
    if flag:
        print("ascending")
elif scale[0] == 8:
    for j in range(8, 0, -1):
        if j != scale[8-j]:
            flag = False
            break
    if flag:
        print("descending")
else:
    flag = False

if not flag:
    print("mixed")

