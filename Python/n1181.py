import sys

input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    s = input().rstrip()
    array.append(s)
array = list(set(array))
array.sort()
array.sort(key=len)

for i in array:
    print(i)
