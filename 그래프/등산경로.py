"""
마을 뒷산의 형태를 나타낸 지도 N*N, 각 구역에 높이 나타남
다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동 가능
등산로의 출발지는 전체 영역에서 가장 낮은 곳이고, 목적지는 가장 높은 곳
출발지와 목적지는 유일

출발지에서 도착지로 갈 수 있는 등산경로 가지수 출력

첫 번째 줄에 N(5<=N<=13)주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.

5
2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100
"""

import sys
input = sys.stdin.readline

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

# 출발지
sx=0
sy=0
min=sys.maxsize

# 도착지
ex=0
ey=0
max=0

n=int(input())
graph= [[0]*n for _ in range(n)]
visited= [[False]*n for _ in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if min>arr[j]:
            sx=i
            sy=j
            min=arr[j]
        if max<arr[j]:
            ex=i
            ey=j
            max=arr[j]
        graph[i][j]=arr[j]
# print(graph)

# 시작점
cnt=0 # 출발지에서 도착지로 갈 수 있는 등산경로 가지수
def dfs(x,y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for i in range(4):
            nextX=x+dr[i]
            nextY=y+dc[i]
            if 0<=nextX<n and 0<=nextY<n and not visited[nextX][nextY]:
                if graph[nextX][nextY]>graph[x][y]: # 높은 구역으로만 이동 가능
                    visited[nextX][nextY]=True
                    dfs(nextX,nextY)
                    visited[nextX][nextY]=False # 바꿔줘야 다른길로 back해서 탐색할 수 있음

visited[sx][sy]=True
dfs(sx,sy)
print(cnt)