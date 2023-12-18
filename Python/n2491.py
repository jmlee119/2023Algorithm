import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
increase = [1] * 100001
decrease = [1] * 100001

for i in range(N - 1):
    if arr[i] <= arr[i + 1]:
        increase[i + 1] += increase[i]
for i in range(N - 1):
    if arr[i] >= arr[i + 1]:
        decrease[i + 1] += decrease[i]
print(increase[: N + 1])
print(decrease[: N + 1])
print(max(max(increase), max(decrease)))
