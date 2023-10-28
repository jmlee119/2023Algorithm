import sys

input = sys.stdin.readline

s = input()
n = int(input())

for _ in range(n):
    alphabet, left, right = map(str, input().split())

    print(s[int(left) : int(right) + 1].count(alphabet))
