import sys

n = int(sys.stdin.readline())

def isPalindrome(a, first, last , count):
    count +=1
    if first >= last :
        return 1, count
    elif a[first] != a[last]:
        return 0, count
    else:
        return isPalindrome (a, first+1 , last-1, count)

for i in range(n):
    a = sys.stdin.readline().rstrip()
    count =0
    check , count =isPalindrome(a, 0, len(a)-1 ,count)
    print(check, count)
