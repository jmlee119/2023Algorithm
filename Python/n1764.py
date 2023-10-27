import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for _ in range(n):
    s = input().rstrip()
    array.append(s)
array2 = []
for _ in range(m):
    s = input().rstrip()
    array2.append(s)
set1 = set(array)
set2 = set(array2)
sets = list(set1 & set2)
sets.sort()
print(len(sets))
for i in sets:
    print(i)
