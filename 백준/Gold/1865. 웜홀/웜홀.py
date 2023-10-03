import sys

input = sys.stdin.readline
TC = int(input())


def bf(start):
    dist[start] = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for next, time in graph[j]:
                if dist[next] > dist[j] + time:
                    dist[next] = dist[j] + time
                    if i == N:
                        return True
    return False


for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    dist = [10001 for _ in range(N + 1)]
    for i in range(M):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for i in range(W):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])
    possible = bf(1)
    if possible:
        print("YES")
    else:
        print("NO")
