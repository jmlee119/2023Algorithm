import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
hap = int(input())

start, end = 0, N - 1
count = 0
while end > start:
    temp = arr[start] + arr[end]
    if temp == hap:
        count += 1
        start += 1
    elif temp < hap:
        start += 1
    else:
        end -= 1
print(count)
