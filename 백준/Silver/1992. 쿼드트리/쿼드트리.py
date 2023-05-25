answer = ""
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(str, input())))


def dfs(x, y, N):
    global answer
    target = graph[x][y]
    for i in range(x, N + x):
        for j in range(y, N + y):
            if target != graph[i][j]:
                answer = answer + "("
                for k in range(2):
                    for l in range(2):
                        cut = N // 2
                        dfs(x + (cut * k), y + (cut * l), cut)
                answer = answer + ")"
                return
    answer = answer + target


# print(graph)
dfs(0, 0, N)
print(answer)
