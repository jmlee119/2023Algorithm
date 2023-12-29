import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))
visited = [[False] * m for i in range(n)]


def dfs(x, y):
    global count
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            if graph[nx][ny] == "X":
                continue
            else:
                if graph[nx][ny] == "P":
                    count += 1
                dfs(nx, ny)


# print(visited)

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            dfs(i, j)

if count == 0:
    print("TT")
else:
    print(count)
