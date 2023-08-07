import sys
from collections import deque
INF=sys.maxsize
dr = [0,0,1,-1]
dc = [1,-1,0,0]

def solution(board):
    answer = 0
    n,m=len(board), len(board[0])
    
    sr=sc=er=ec=-1
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                sr,sc = i,j
            elif board[i][j]=='G':
                er,ec=i,j
    
    dist = [[INF]*m for _ in range(n)]
    dist[sr][sc] = 0

    q = deque([(sr, sc)])
    while q:
    
        if dist[er][ec] != INF:
            return dist[er][ec]

        r, c = q.popleft()
        
        for d in range(4):
            nr,nc = r,c
            while 0 <= nr+dr[d]< n and 0 <=nc+dc[d]< m and board[nr+dr[d]][nc+dc[d]]!='D':
                nr, nc = nr+dr[d], nc+dc[d]
                
            if  dist[r][c] < dist[nr][nc]:
                dist[nr][nc]=dist[r][c]+1
                q.append((nr, nc))

    return -1