import sys

input = sys.stdin.readline
arr = []
for _ in range(3):
    n = int(input())
    arr.append(n)

answer = arr[0] * arr[1] * arr[2]

ans = []
for i in range(10):
    ans.append(str(answer).count(str(i)))

for i in ans:
    print(i)
