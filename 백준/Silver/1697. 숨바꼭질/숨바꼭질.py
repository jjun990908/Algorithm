import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for nv in (v-1, v+1, 2*v):
            if 0 <= nv < MAX and not array[nv]:
                array[nv] = array[v] + 1
                q.append(nv)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))