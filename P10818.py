import sys

input = sys.stdin.readline
input()
nums = list(map(int, input().split()))
print(min(nums), max(nums))
