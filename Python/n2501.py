import sys
input = sys.stdin.readline
list = [1]
n,k = map(int,input().rstrip().split())
for i in range(1,n//2):
    if(n%i==0):
        list.append(i)
    
print(list)