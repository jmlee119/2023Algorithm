import sys

dic = {}

N = int(input())
for _ in range(N):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1


max_value = max(dic.values())

best = []
for key, value in dic.items():
    if max_value == value:
        best.append(key)

best.sort()
print(best[0])
