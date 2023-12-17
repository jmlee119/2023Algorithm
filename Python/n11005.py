N, B = map(int, input().split())
JIN = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = ""
while N > 0:
    s += str(JIN[N % B])
    N //= B

print(s[::-1])
