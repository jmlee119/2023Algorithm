import sys

input = sys.stdin.readline
N, X = map(int, input().split())
arr = list(map(int, input().split()))
count = 1
window = sum(arr[:X])
ans = window

for i in range(X, N):
    window += arr[i]
    window -= arr[i - X]
    if ans < window:
        count = 1
        ans = window
    elif ans == window:
        count += 1


if ans == 0:
    print("SAD")
else:
    print(ans)
    print(count)
