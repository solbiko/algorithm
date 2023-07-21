from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    board=[[-1]*102 for _ in range(102)]
    
    # 사각형좌표 그리기
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2: # 내부 0으로 채우기
                    board[i][j]=0
                elif board[i][j]!=0: # 다른 직사각형의 내부가 아니면서 테두리일 때 1
                    board[i][j]=1
    
    def bfs(i,j):
        
        q = deque()
        q.append([i,j])
        visited=[[1]*102 for _ in range(102)]

        while q:
            x,y=q.popleft()

            if x==itemX*2 and y==itemY*2:
                return visited[x][y]//2

            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]

                if board[nx][ny]==1 and visited[nx][ny]==1:
                    q.append([nx,ny])
                    visited[nx][ny]=visited[x][y]+1

                
    return bfs(characterX*2, characterY*2)