sum=0 
hak = 0.0
for i in range(1,21):
    # a =input()
    # b =float(input())
    # c = input()
    a,b,c = list(input().split())
    b = float(b)
    if (c=='A+'):
        sum+=4.5*b
        hak+=b
    elif (c=='A0'):
        sum+=4.0*b
        hak+=b
    elif (c=='B+'):
        sum+=3.5*b
        hak+=b
    elif (c=='B0'):
        sum+=3.0*b
        hak+=b
    elif (c=='C+'):
        sum+=2.5*b
        hak+=b
    elif (c=='C0'):
        sum+=2.0*b
        hak+=b
    elif (c=='D+'):
        sum+=1.5*b
        hak+=b
    elif (c=='D0'):
        sum+=1.0*b
        hak+=b
    elif (c=='F'):
        sum+=0.0*b
        hak+=b
    else:
        continue

print(sum/hak)