import sys
input = sys.stdin.readline

s1 = set([])
s2 = set([])
m,n = map(int, input().rstrip().split())
list1 = list(map(int, input().rstrip().split()))
s1.update(list1)
list2 = list(map(int, input().rstrip().split()))
s2.update(list2)

l1 = list(s1-s2)
l2 = list(s2-s1)

print(len(l1)+len(l2))