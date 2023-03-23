import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def main(w, h):    
    answer = 0
    board = [list(map(int , input().rstrip().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]   
    def dfs(x, y, w, h):
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, w, h)

    for i in range(h):
        for j in range(w):
            if board[i][j] and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, w, h)
                answer += 1

    return answer

while True:
    w,h = map(int, input().rstrip().split())
    if w + h == 0 : break
    print(main(w, h))