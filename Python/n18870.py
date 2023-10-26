import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

set_arr = list(set(arr))
set_arr.sort()

dic = {set_arr[i]: i for i in range(len(set_arr))}

for i in arr:
    print(dic[i], end=" ")
