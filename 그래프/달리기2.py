""""
매 초마다 진영이는 위, 아래, 오른쪽, 왼쪽 중에서 이동할 방향을 하나 고르고, 그 방향으로 최소 1개, 최대 K개의 빈 칸을 이동한다.
시작점 (x1, y1)과 도착점 (x2, y2)가 주어졌을 때, 시작점에서 도착점으로 이동하는 최소 시간

체육관의 크기 N과 M, 1초에 이동할 수 있는 칸의 최대 개수 K
N개의 줄에는 체육관의 상태가 주어진다. 체육관의 각 칸은 빈 칸 또는 벽이고, 빈 칸은 '.', 벽은 '#'으로 주어진다.
마지막 줄에는 네 정수 x1, y1, x2, y2가 주어진다. 두 칸은 서로 다른 칸이고, 항상 빈 칸이다.

(x1, y1)에서 (x2, y2)로 이동하는 최소 시간을 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.
3 4 4
....
###.
....
1 1 3 1
"""
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m,k=map(int, input().split())
a=[input() for _ in range(n)]
x1,y1,x2,y2=map(int, input().split())

dist = [[-1] * (m) for _ in range(n)]
dist[x1-1][y1-1] = 0
q = deque([(x1-1,y1-1)])

while q:
    x,y = q.popleft()
    for d in range(4):
        for nk in range(1,k+1):
            nx,ny=x+nk*dx[d],y+nk*dy[d]
            if not (0<=nx<n and 0<=ny<m) or a[nx][ny] == '#':  break
            if -1 != dist[nx][ny] <= dist[x][y]:  break
            if -1 != dist[nx][ny]:  continue
            dist[nx][ny]=dist[x][y]+1
            q.append((nx,ny))

# for i in range(n):
#     for j in range(m):
#         print(dist[i][j], end="  ")
#     print()

print(dist[x2-1][y2-1])