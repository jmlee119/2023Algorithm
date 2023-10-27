import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dic_1, dic_2 = {}, {}
for i in range(1, n + 1):
    s = input().rstrip()
    dic_1[i] = s
    dic_2[s] = i

# print(dic_1)
# print(dic_2)

for _ in range(m):
    i = input().rstrip()
    if i.isdigit():
        print(dic_1[int(i)])
    else:
        print(dic_2[i])
