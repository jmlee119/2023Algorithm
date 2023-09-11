N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

coin.reverse()
count = 0
for i in coin:
    if i <= K:
        count += K // i
        K = K % i
        if K == 0:
            break

print(count)
