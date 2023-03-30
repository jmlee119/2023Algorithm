import sys
input = sys.stdin.readline
list = []
n,k = map(int,input().rstrip().split())
for i in range(1,n):
    if(n%i==0):
        list.append(i)
        if (i != n//i):
            list.append(n//i)
    
list.sort()
if (k >=len(list)):
    print(0)
else:
    print(list[k-1])