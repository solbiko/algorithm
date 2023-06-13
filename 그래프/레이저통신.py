"""
W×H 크기의 지도
레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다.
빈 칸은 '.', 벽은 '*'로 나타냈다. 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.
C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력
7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......
"""
import sys
input=sys.stdin.readline
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

W,H=map(int, input().split())
graph = []
conn=[]
for i in range(H):
    graph.append(input())
    for j in range(W):
        if graph[i][j]=='C':
            conn.append((i,j))

start,end=conn
visited = [[-1]*W for _ in range(H)]
visited[start[0]][start[1]]=0
queue=deque()
queue.append(start)

while queue:
    r,c=queue.popleft()

    for k in range(4): # 네방향 탐색
        nr,nc=r+dx[k],c+dy[k]

        while 0<=nr<H and 0<=nc<W:  # 격자판
            if graph[nr][nc]=='*':
                break  # 벽
            if visited[nr][nc]==-1:
                queue.append((nr,nc))
                visited[nr][nc]=visited[r][c]+1
                # 한방향 계속 탐색
            nr+=dx[k]
            nc+=dy[k]


print(visited[end[0]][end[1]]-1)