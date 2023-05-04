"""
7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력
경로수는 출발점에서 도착점까지 가는데 이동한 횟수
출발점은 격자의 (1, 1) 좌표이고, 탈 출 도착점은 (7, 7)좌표
격자판의 1은 벽이고, 0은 도로

0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0

도착할 수 없으면 -1를 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

graph= [list(map(int, input().split())) for _ in range(7)]
d = [[0]*7 for _ in range(7)]

queue=deque()
queue.append((0,0))
graph[0][0]=1 # 한번 방문한 곳은 벽으로 만듬

while queue:
    r,c=queue.popleft()
    for i in range(4): # 상하좌우 탐색
        x= r+dr[i]
        y= c+dc[i]

        if 0<=x<7 and 0<=y<7 and d[x][y]==0: # 좌표 유효성 검사
            graph[x][y]=1 # 방문한 곳 벽으로 만듬
            d[x][y]=d[r][c]+1
            queue.append((x,y))

print(d[6][6] if d[6][6]!=0 else -1)