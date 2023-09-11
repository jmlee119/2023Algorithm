import sys

input = sys.stdin.readline

n = int(input())
value = [[0] * 2 for _ in range(n)]
# print(value)
list = list(map(int, input().rstrip().split()))
for idx, i in enumerate(list):
    value[idx][0] = i
    value[idx][1] = idx + 1
value = sorted(value, key=lambda a: a[0])

sum = 0
for i in range(n + 1):
    count = 0
    for a in range(i):
        count += value[a][0]
    sum += count

print(sum)
