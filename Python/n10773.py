import sys
input = sys.stdin.readline

n = int(input())
list =[]
for _ in range(n):
    x= int(input())
    if x==0:
        list.pop()
    else:
        list.append(x)
sum=0
for i in range(len(list)):
    sum = sum + list[i]

print(sum)
