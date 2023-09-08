from collections import deque

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    line = list(map(int, input().split()))
    currentNode = line[0]
    idx = 1
    while line[idx] != -1:
        node = line[idx]
        cost = line[idx + 1]
        graph[currentNode].append((node, cost))
        idx += 2


def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited = [-1] * (V + 1)
    visited[start] = 0
    result = [0, 0]
    while queue:
        node, cost = queue.popleft()

        for curNode, curCost in graph[node]:
            if visited[curNode] == -1:
                sum = cost + curCost
                queue.append((curNode, sum))
                visited[curNode] = 1
                if result[1] < sum:
                    result[0] = curNode
                    result[1] = sum

    return result


node, cost = bfs(1)
print(bfs(node)[1])
