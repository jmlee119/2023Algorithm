arr=[]
r =''
for i in range(5):
    arr.append(input())
for i in range(15):
    for j in range(5):
        if len(arr[j])>i:
            r+= arr[j][i]

print(r)