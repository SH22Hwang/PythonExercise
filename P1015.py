def deci_to_any(n, b):
    str_binary = ""
    while n>0:
         str_binary += str(n%b)
         n = n//b
    return str_binary

result = deci_to_any(140, 8)
print(result[::-1])

# def deci_to_any(n, b):
#     str_binary = ""
#     while n > 0:
#          str_binary = str(n % b) + str_binary
#          n = n // b
#
#     return str_binary
#
# result = deci_to_any(140, 8)
# print(result)