import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    ans += i * i

print(ans % 10)
