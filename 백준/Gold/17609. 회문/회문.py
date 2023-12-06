from collections import deque
import heapq
import sys

input = sys.stdin.readline


num = int(input())
for _ in range(num):
    text = input().strip()
    left, right = 0, len(text) - 1
    check = 0

    for _ in range(len(text)):
        if left >= right:
            break
        if text[left] == text[right]:
            left += 1
            right -= 1
            continue

        if text[left] == text[right - 1]:
            temp = text[left:right]
            if temp[:] == temp[::-1]:
                check = 1
                break

        if text[left + 1] == text[right]:
            temp = text[left + 1 : right + 1]
            if temp[:] == temp[::-1]:
                check = 1
                break

        check = 2
        break

    print(check)
