"""
n개의 도시(2~100)
m 버스의 개수(1~100,000)
모든 도시의 쌍에 관해 가는 데 필요한 비용의 최솟값


a(시작도시) b(도착도시) c(비용 1~100,000)
시작도시와 도착 도시를 연결하는 노선은 1개가 아닐 수 있다

n개의 줄 출력
"""
import sys

# 도시 개수
n = int(input())

# 버스 개수
m = int(input())

# 인접행렬
d = array = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]

# 인접 행렬에 시작 도시와 종료 도시가 같은 자리에 0 저장
for i in range(1, n+1):
    d[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if d[a][b] > 0:
        d[a][b] = c

# print(d)

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if d[s][e] > d[s][k] + d[k][e]:
                d[s][e] = d[s][k] + d[k][e]


for i in range(1, n+1):
    for j in range(1, n + 1):
        if d[i][j] != sys.maxsize:
            print(d[i][j], end=" ")
        else:
            print(0, end=" ")
    print()