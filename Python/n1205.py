import sys

input = sys.stdin.readline

N, Tae_score, P = map(int, input().split())
if N != 0:
    score = list(map(int, input().split()))
    score.append(Tae_score)
    score.sort(reverse=True)
    Tae_idx = score.index(Tae_score) + 1

    if Tae_idx > P:
        print(-1)
    else:
        if N == P and Tae_score == score[-1]:
            print(-1)
        else:
            print(Tae_idx)
else:
    print(1)
