import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
arr =[0] * (n+1)
for i in range(m):
    a,b,c = map(int,input().rstrip().split())
    for j in range(a,b+1):
        arr[j] =c


for i in range(1,len(arr)):
    print(arr[i], end=' ')