import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
arr =[i for i in range(1,n+1)]
for i in range(m):
    a , b = map(int,input().rstrip().split())
    temp = arr[a-1:b]
    temp.reverse()
    arr[a-1:b] = temp

for i in range(n):
    print(arr[i],end =' ')
        