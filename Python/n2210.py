import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

answer = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []

for _ in range(5):
    graph.append(list(map(str, input().split())))


def dfs(x, y, number):
    if len(number) == 6:
        if number not in answer:
            answer.append(number)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, number + graph[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(answer))
