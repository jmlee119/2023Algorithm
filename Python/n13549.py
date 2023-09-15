import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
visited[n] = True
hq = [([0, n])]

while hq:
    t, x = heapq.heappop(hq)
    print(t, x)
    if x == k:
        print(t)
        break

    # 순간이동을 먼저 처리해야 한다.
    # 그래야 1 2 와 같은 입력에 0을 출력할 수 있다.
    dx = x * 2
    if dx < len(visited) and not visited[dx]:
        visited[dx] = True
        heapq.heappush(hq, (t, dx))

    for i in (x + 1, x - 1):
        if i >= 0 and i < len(visited) and not visited[i]:
            visited[i] = True
            heapq.heappush(hq, (t + 1, i))
