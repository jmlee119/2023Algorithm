import sys
from itertools import product

input = sys.stdin.readline

N, k = map(int, input().split())
arr = list(map(str, input().split()))
lenght = len(str(N))
new_arr = []

while True:
    pro = list(product(arr, repeat=lenght))
    for i in pro:
        ans = int("".join(i))
        if ans <= N:
            new_arr.append(ans)
    if lenght <= 1:
        print(max(new_arr))
        break
    else:
        lenght -= 1
