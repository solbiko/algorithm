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
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
W,H=map(int, input().split())
a=[input() for _ in range(H)]
sx=sy=ex=ey=-1
for i in range(H):
    for j in range(W):
        if a[i][j] == 'C':
            if sx == -1:
                sx,sy = i,j
            else:
                ex,ey = i,j
dist = [[-1]*W for _ in range(H)]
q = deque()
dist[sx][sy] = 0
q.append((sx,sy))

while q:
    x,y = q.popleft()

    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        # 한 방향으로 쭉 감
        while 0<=nx<H and 0 <=ny<W:
            if a[nx][ny] == '*':  # 벽
                break
            if dist[nx][ny] == -1:  # 방문하지 않았다면
                dist[nx][ny]=dist[x][y]+1  # 직선의 길이 +1
                q.append((nx,ny))
            nx += dx[k]
            ny += dy[k]

for i in range(H):
    for j in range(W):
        print(dist[i][j], end="  ")
    print()
print(dist[ex][ey]-1)