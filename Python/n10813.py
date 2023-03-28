import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
arr =[i for i in range(1,n+1)]
for i in range(m):
    temp =0
    a,b = map(int,input().rstrip().split())
    a = a-1
    b = b-1
    temp = arr[a] 
    arr[a] = arr[b]
    arr[b] = temp

for i in range(len(arr)):
    print(arr[i], end=' ')