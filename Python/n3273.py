import sys

input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().rstrip().split())))
x = int(input())
count = 0
start, end = 0, n - 1

while start < end:
    sum = a[start] + a[end]
    if sum == x:
        count += 1
        start += 1
    elif sum < x:
        start += 1
    else:
        end -= 1

print(count)
