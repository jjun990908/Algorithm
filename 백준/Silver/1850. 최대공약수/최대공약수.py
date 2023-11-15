from collections import deque
import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print("1" * gcd(a, b))
