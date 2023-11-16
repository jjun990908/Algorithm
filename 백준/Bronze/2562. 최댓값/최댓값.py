import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(9)]

print(max(nums))
temp = nums.index(max(nums))
print(temp+1)