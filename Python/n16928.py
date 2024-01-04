import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())


def bfs():
    q = deque([1])
    visited[1] = True
    while q:
        x = q.popleft()

        for i in range(1, 7):
            next = x + i
            if 0 < next <= 100 and not visited[next]:
                if next in ladder.keys():
                    next = ladder[next]

                if next in snake.keys():
                    next = snake[next]

                if not visited[next]:
                    board_cnt[next] = board_cnt[x] + 1
                    visited[next] = True
                    q.append(next)


ladder = dict()
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b

snake = dict()
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b

visited = [False] * 101
board_cnt = [0] * 101
bfs()
print(board_cnt[100])
