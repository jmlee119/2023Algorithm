import sys

input = sys.stdin.readline
n = int(input())
dic = {}

for _ in range(n):
    name, memo = map(str, input().split())
    dic[name] = memo

for key, value in dic.items():
    if value == "enter":
        print(key)
