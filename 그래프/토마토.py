"""
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향 에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
현수는 창고에 보관된 토마토들이 며칠이 지나 면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다. 단, 2 ≤ M, N ≤ 1,000 이다.
둘째 줄부터 N개의 줄 에는 상자에 담긴 토마토의 정보가 주어진다.
1:익은 토마토
0:익지 않은 토마토
-1:빈칸

6 4
0 0 -1 0 0 0
0 0 1 0 -1 0
0 0 -1 0 0 0
0 0 0 0 -1 1

토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력, 토마토가 모두 익지는 못하는 상황이면 -1을 출력
"""
import sys
from collections import deque
input=sys.stdin.readline

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dx=[0,1,0,-1]
dy=[1,0,-1,0]

m,n=map(int,input().split()) # 상자 가로, 세로
graph=[list(map(int, input().split())) for _ in range(n)]

dist=[[0]*m for _ in range(n)] # 익는 시간 저장

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

while queue:
    x,y=queue.popleft()

    for d in range(4):
        nextX= x+dx[d]
        nextY= y+dy[d]
        if 0<=nextX<n and 0<=nextY<m and graph[nextX][nextY]==0: # 안익은 인접 토마토
            graph[nextX][nextY]=1 # 익힘
            dist[nextX][nextY]=dist[x][y]+1 # 익은 시간 저장
            queue.append((nextX,nextY))

flag = 1 # 안익은 토마토 체크
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            flag=0

if flag==1: # 다 익음 : 모두 익을 때까지의 최소 날짜 출력
    res = 0
    for i in range(n):
        for j in range(m):
            if dist[i][j]>res:
                res=dist[i][j]
    print(res)
else: # 안익은 토마토있음
    print(-1)

