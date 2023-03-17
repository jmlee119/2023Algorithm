def avg(*args):
    sum=0
    for i in args:
        sum= sum + i
    return sum/len(args)

a=avg(4,5,7,8,9,5,4,8)
print(a)