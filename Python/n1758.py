import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)

arr = sorted(arr, reverse=True)
result = 0
for idx, i in enumerate(arr):
    # print(idx, i)
    ans = i - idx
    if ans > 0:
        result += ans


print(result)
