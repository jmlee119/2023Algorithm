INF = int(1e9)  # 무한대 값 설정

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

# 도시 간의 최소 비용을 저장할 2차원 배열 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 버스 정보 입력 및 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 노선에 여러 버스가 있을 수 있으므로 최소 비용만 남기도록 함
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드-와샬 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # i에서 j로 가는 경로보다 i에서 k를 거쳐 j로 가는 경로가 더 짧으면 업데이트
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=" ")  # 도달할 수 없는 경우 0 출력
        else:
            print(graph[i][j], end=" ")  # 최소 비용 출력
    print()  # 줄 바꿈
