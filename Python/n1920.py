import sys
input = sys.stdin.readline
def Binary(a, start, end, target):
    find = False
    while (start <= end):
        mid = (start+end)//2
        if a[mid]== target:
            find= True
            break
        elif a[mid] > target:
            end =mid-1
        elif a[mid] < target:
            start= mid+1
        
    if find == True:
        return 1
    else:
        return 0
        
n = int(input())
a = list(map(int, input().rstrip().split()))
a.sort()
m = int(input())
find = list(map(int, input().rstrip().split()))

for i in find:  
    target = i
    print(Binary(a,0,len(a)-1,target))
    