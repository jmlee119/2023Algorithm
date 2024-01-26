import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dicts = dict()
ans = 0

for _ in range(N):
    keywords = input().rstrip()
    dicts[keywords] = 1
    ans += 1

for _ in range(M):
    blog = list(map(str, input().rstrip().split(",")))
    for i in blog:
        if i in dicts.keys():
            if dicts[i] == 1:
                dicts[i] = 0
                ans -= 1

    print(ans)
