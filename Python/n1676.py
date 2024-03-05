import sys
input =sys.stdin.readline

n= int(input())
ans = 1

for i in range(1,n+1):
    ans = ans * i

ans = list(str(ans))
ans_arr = ans[::-1]
cnt= 0
for i in ans_arr:
    if i =='0':
        cnt +=1
    else:
        break


print(cnt)