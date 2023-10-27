import sys

input = sys.stdin.readline
n = int(input())
dic = {}
answer = []
for _ in range(n):
    name, memo = map(str, input().split())
    dic[name] = memo

for key, value in dic.items():
    if value == "enter":
        answer.append(key)

answer.sort(reverse=True)
for i in answer:
    print(i)
