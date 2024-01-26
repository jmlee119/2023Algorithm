import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = [0] * N
for i in range(N):
    cnt = 0
    p = arr[i]
    for j in range(N):
        if cnt == p and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            cnt += 1


print(*ans)
