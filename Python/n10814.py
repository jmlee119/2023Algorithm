import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    age, name = input().split()
    array.append([age, name])

array.sort(key=lambda x: int(x[0]))

for i in array:
    print(" ".join(i))
