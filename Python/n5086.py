def Pan(a, b):
    if (a>b):
        if(a%b==0):
            print("multiple")
        else:
            print("neither")
    else:
        if(b%a==0):
            print("factor")
        else:
            print("neither")

while(True):
    a,b = map(int, input().split())
    if(a==0 or b==0):
        break
    else:
        Pan(a,b)
    