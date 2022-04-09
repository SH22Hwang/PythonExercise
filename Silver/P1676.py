import math

f = reversed(str(math.factorial(int(input()))))
result = 0

for x in f:
    if x == '0':
        result += 1
    else:
        break

print(result)
