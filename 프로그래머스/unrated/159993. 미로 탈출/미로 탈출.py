from collections import deque
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def solution(maps):
    answer = 0
    
    n,m=len(maps), len(maps[0])
    
    def BFS(start, end):
        
        i,j=start
        k,l=end
        
        visited= [[0]*m for i in range(n)] # BFS 시 방문 여부 저장 리스트
        visited[i][j]=1

        queue=deque()
        queue.append([i,j])

        while queue:
            r,c=queue.popleft()
            
            for d in range(4):
                nextR= r+dr[d]
                nextC= c+dc[d]
                
                if 0<=nextR<n and 0<=nextC<m and visited[nextR][nextC]==0 and maps[nextR][nextC]!='X':
                        visited[nextR][nextC]=visited[r][c]+1 # 방문 표시
                        queue.append([nextR,nextC])
        return visited[k][l]-1
    
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S': start = (i, j)
            elif maps[i][j] == 'L': lever = (i, j)
            elif maps[i][j] == 'E': end = (i, j)
    
    
    stol = BFS(start, lever)
    ltoe = BFS(lever, end)
    
    if stol != -1 and ltoe != -1:
        return stol + ltoe
    else:
        return -1
