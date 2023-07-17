import sys
from collections import deque

dr=[1,-1,0,0]
dc=[0,0,1,-1]
answer = sys.maxsize

def solution(maps):
    n=len(maps)
    m=len(maps[0])

    def bfs(i,j):
        queue=deque()
        queue.append((i,j))
        
        while queue:
            r,c=queue.popleft()

            for k in range(4):
                nr= r+dr[k]
                nc= c+dc[k]
                if 0<=nr<n and 0<=nc<m and maps[nr][nc] ==1:
                    maps[nr][nc]=maps[r][c]+1
                    queue.append((nr,nc))
                    
    bfs(0,0)
    answer=maps[n-1][m-1]
    return answer if answer!=1 else -1


