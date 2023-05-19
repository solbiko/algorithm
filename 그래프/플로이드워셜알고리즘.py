"""
N개의 도시가 주어지고, 각 도시들을 연결하는 도로와 해당 도로를 통행하는 비용이 주어질 때
모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최소값

첫 번째 줄에는 도시의 수N(N<=100)과 도로수 M(M<=200)가 주어지고,
M줄에 걸쳐 도로정보 와 비용(20 이하의 자연수)이 주어진다. 만약 1번 도시와 2번도시가 연결되고 그 비용이 13이 면 “1 2 13”으로 주어진다.
5 8
1 2 6
1 3 3
3 2 2
2 4 1
2 5 13
3 4 5
4 2 3
4 5 7


모든 도시에서 모든 도시로 이동하는데 드는 최소 비용을 아래와 같이 출력한다.
자기자신으로 가는 비용은 0입니다. i번 정점에서 j번 정점으로 갈 수 없을 때는 비용을 “M"으 로 출력합니다.
0 5 3 6 13
M 2 0 3 10
M 3 M 0 7
M M M M 0
"""
import sys
input=sys.stdin.readline

#도시수, 도로수
n,m = map(int,input().split())

# 인접행렬
d = array = [[sys.maxsize for j in range(n)] for i in range(n)]
for i in range(n):
    d[i][i] = 0

for _ in range(m):
  i,j,w = list(map(int, input().split()))
  d[i-1][j-1]=w

for k in range(n): # 경유지 k
    for s in range(n):
        for e in range(n):
            if d[s][k]!= sys.maxsize and d[k][e]!= sys.maxsize :
                d[s][e]=min(d[s][e], d[s][k]+d[k][e])
# print(d)

for i in range(n):
    for j in range(n):
        print(d[i][j] if d[i][j]!=sys.maxsize else "M", end=" ")
    print()
