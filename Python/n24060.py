import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
a = list(map(int, input().rstrip().split()))

def merge_sort(a, left,right):
    if left <right and count <=m:
        mid = (left +right) //2
        merge_sort(a,left,mid)
        merge_sort(a,mid+1,right)
        merge(a,left,mid,right)


def merge(a,left,mid,right):
    tmp = []
    global result,count
    i ,j,t = left ,mid+1, 1 
    while(i <= mid and j <= right ):
        if (a[i] <= a[j]):
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while (i <=mid):
        tmp.append(a[i])
        i += 1
    while (j <=right):
        tmp.append(a[j])
        j += 1
    i, t = left, 0
    
    while i <= right:
        a[i] = tmp[t]
        count +=1
        if count == m:
            result = a[i]
            break
        i += 1
        t += 1

count = 0
result = -1

merge_sort(a, 0 , n-1)
print(result)