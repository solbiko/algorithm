"""
벨만-포드

N개의 도시(1~500), 한 도시에서 출발해 다른 도시에 도착하는 버스 M개(1~6,000)
A 시작도시 B 도착도시(1~N)  C 걸린시간(-10,000~10,000)

1번 도시에서 출발해 나머지 도시로 가는 가장 빠른 시간

시간을 무한히 오래전으로 되돌릴 수 있으면 1번째 줄에 -1출력 (음수간선싸이클 있으면)
아니면 n-1개 줄에 걸쳐 각줄의 1번 도시에서 출발해 2번 도시, 3번 도시,...,N번 도시로 가는 가ㅏㅇ 빠른 시간 순서대로 출력
경로 없으면 -1 출력
"""

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())


# 에지 리스트
graph = []
for i in range(m):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

# print(graph)

# 최단 경로 리스트
d = [INF] * (n+1)
d[1] = 0

# print(d)


cycleYn = False

for i in range(1, n+1):
    for start, end, weight in graph:
        if d[start] != INF:
            d[end] = d[start] + weight if d[end] > d[start] + weight else d[end]

for start, end, weight in graph:
    cycleYn = True if d[end] > d[start] + weight else False

if cycleYn:
    print(-1)
else:
    for i in range(2, n+1):
        if d[i] != INF:
            print(d[i])