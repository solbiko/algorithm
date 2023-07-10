dr = (1, 0, -1, 0)
dc = (0, -1, 0, 1)

def solution(grid): # 빛의 경로 싸이클 길이 리스트 오름차순 리턴
    answer = []
    
    """
    0,0 에서 시작
    네방향 탐색 bfs
    """
    lr, lc = len(grid), len(grid[0])
    print(lr,lc)
    
    # 네방향 방문 기록
    visited=[[[False]*4 for _ in range(lc)] for __ in range(lr)]
    
    for r in range(lr):
        for c in range(lc): # 모든 좌표
            for d in range(4): # 네방향
                
                if visited[r][c][d]:
                    continue
                    
                cnt=0 
                nr,nc=r,c
                while not visited[nr][nc][d]:
                    visited[nr][nc][d] = True
                    cnt+=1
                    if grid[nr][nc] == "S":
                        pass
                    elif grid[nr][nc]=="L": # L의 경우 반시계방향
                        d=(d-1)%4
                    elif grid[nr][nc]=="R": # R의 경우 시계방향
                        d=(d+1)%4
                    nr=(nr+dr[d])%lr
                    nc=(nc+dc[d])%lc
                    
                answer.append(cnt)
                
    return sorted(answer)