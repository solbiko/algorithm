import copy
from collections import deque

dr=[0,1,0,-1]
dc=[1,0,-1,0]

def solution(game_board, table):
    g_n=len(game_board)

    def BFS(i,j, board, flag, visited):
        queue=deque()
        obj=[]
        
        queue.append([i,j])
        obj.append([i,j])
        visited[i][j]=True

        while queue:
            r,c=queue.popleft()
            for d in range(4):
                tempR=dr[d]
                tempC=dc[d]
                nextR= r+tempR
                nextC= c+tempC
                while 0<=nextR<g_n and 0<=nextC<g_n: # 격자
                    if not visited[nextR][nextC] and board[nextR][nextC]==flag:
                        # 연결된 새로운 노드가 확인되면 저장
                        visited[nextR][nextC]=True # 방문 표시
                        obj.append([nextR,nextC])
                        queue.append([nextR,nextC])
                    else:
                        break
                    if tempR<0:
                        tempR-=1
                    elif tempR>0:
                        tempR+=1
                    elif tempC<0:
                        tempC-=1
                    elif tempC>0:
                        tempC+=1
        return obj

    
    def group_to_matrix(group):
        min_x = min(group, key=lambda x:x[0])[0]
        min_y = min(group, key=lambda x:x[1])[1]

        for k in range(len(group)) :
            group[k][0] -= min_x
            group[k][1] -= min_y

        max_x = max(group, key=lambda x:x[0])[0] + 1
        max_y = max(group, key=lambda x:x[1])[1] + 1

        matrix = [[0] * max_y for _ in range(max_x)]
        for x,y in group :
            matrix[x][y] = 1
        return matrix
    
    
    """ 1. table 퍼즐조각 배열 만들기 (n*n) """
    puzzle_list=list([]) # 퍼즐 리스트
    visited= [[False]*g_n for i in range(g_n)]
    for i in range(g_n): # 구분 작업 수행
        for j in range(g_n): 
            if table[i][j] != 0 and not visited[i][j]:
                # BFS를 실행해 하나의 퍼즐조각 정보 가져오기
                group = copy.deepcopy(BFS(i,j, table, 1, visited))
                puzzle_list.append(group_to_matrix(group))

                
    """ 2. 게임 보드에서 빈칸 배열 만들기 (n*n) """    
    blank_list=list([]) # 빈칸 리스트
    visited= [[False]*g_n for i in range(g_n)]
    for i in range(g_n): # 구분 작업 수행
        for j in range(g_n):
            if game_board[i][j] != 1 and not visited[i][j]:
                # BFS를 실행해 하나의 빈칸 정보 가져오기
                group = copy.deepcopy(BFS(i,j, game_board, 0, visited))
                blank_list.append(group_to_matrix(group))
                
    
    """ 3. 퍼즐조각 돌면서 빈칸 비교, 맞는지 붙여보기(90도 회전 3번까지 총 4번 체크) """
    
    def rotate(puzzle):
        c, r = len(puzzle), len(puzzle[0])
        temp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                temp[i][j] = puzzle[c-1-j][i]
        return temp
    
    
    answer = 0
    for p in puzzle_list:
        for b in blank_list:
            
            if len(p)*len(p[0]) == len(b)*len(b[0]):
                
                find = False
                for _ in range(4):
                    if p==b:
                        find = True
                        for row in p:
                            answer += row.count(1) # 퍼즐조각 붙어진 곳 카운트
                        b[0][0] = -1
                        break
                    else :
                        p = rotate(p)
                        
                if find : break

    return answer
