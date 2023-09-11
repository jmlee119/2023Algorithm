import sys

input = sys.stdin.readline

n = int(input())

time = [[0] * 2 for _ in range(n)]

for i in range(n):
    start, end = map(int, input().rstrip().split())
    time[i][0] = start
    time[i][1] = end
time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

last = 0
count = 0
for i, j in time:
    if i >= last:
        count += 1
        last = j
print(count)
