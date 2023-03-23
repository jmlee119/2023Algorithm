num = int(input())
i=2
while True:
    if(num%i==0):
        num = num/i
        print(i)
    elif(num==1):
        break
    else:
        i = i+1
        
        