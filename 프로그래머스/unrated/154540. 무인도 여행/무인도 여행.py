import copy
from collections import deque
dr=[0,1,0,-1]
dc=[1,0,-1,0]

def solution(maps):
    answer=[]
    
    n,m=len(maps), len(maps[0])
    visited= [[False]*m for i in range(n)] # BFS 시 방문 여부 저장 리스트

    def BFS(i,j):
        cnt=0

        queue=deque()
        queue.append([i,j])
        cnt+=int(maps[i][j])
        visited[i][j]=True

        while queue:
            r,c=queue.popleft()
            for d in range(4):
                tempR=dr[d]
                tempC=dc[d]
                nextR= r+tempR
                nextC= c+tempC
                if 0<=nextR<n and 0<=nextC<m:
                    if not visited[nextR][nextC] and maps[nextR][nextC]!='X':
                        visited[nextR][nextC]=True # 방문 표시
                        cnt+=int(maps[nextR][nextC]) # 식량 수 카운트
                        queue.append([nextR,nextC])
                  
        return cnt

    # 섬 구분
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                total_cnt = copy.deepcopy(BFS(i,j)) # 총 식량
                answer.append(total_cnt)
                
    if answer:
        return sorted(answer)
    else:
        return [-1]
