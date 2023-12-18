import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
increase = [1] * 1001
decrease = [1] * 1001

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i - 1, -1):
        if arr[i] > arr[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
result = [0 for i in range(N + 1)]
for i in range(N):
    result[i] = (increase[i] + decrease[i]) - 1

# print
print(max(result))
