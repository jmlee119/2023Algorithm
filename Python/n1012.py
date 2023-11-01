import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

Testcase = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dfs(nx, ny)


for _ in range(Testcase):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j)
                result += 1

    print(result)
