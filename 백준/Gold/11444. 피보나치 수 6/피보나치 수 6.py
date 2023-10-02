from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
matrix = [[1, 1], [1, 0]]


def multiple(mat1, mat2):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] * mat2[k][j] % 1000000007
    return res


def power(a, b):
    if b == 1:
        return a
    else:
        temp = power(a, b // 2)
        if b % 2 == 0:
            return multiple(temp, temp)
        else:
            return multiple(multiple(temp, temp), a)


answer = power(matrix, N)
print(answer[0][1] % 1000000007)
