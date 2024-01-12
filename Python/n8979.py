import sys

input = sys.stdin.readline

N, K = map(int, input().split())
medal = []
ans = []


for _ in range(N):
    medal.append(list(map(int, input().split())))

medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [medal[i][0] for i in range(N)].index(K)
for i in range(N):
    if medal[idx][1:] == medal[i][1:]:
        print(i + 1)
        break
