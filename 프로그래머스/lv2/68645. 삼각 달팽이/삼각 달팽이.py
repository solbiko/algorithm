def solution(n):
    
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)] # 삼각형
 
    r,c = 0,0 # 좌표
    
    i = 1
    for d in range(n): # 방향
        for _ in range(n-d):
            if d%3 == 0: # 하
                r += 1
            elif d%3 == 1: # 우
                c += 1
            else: # 상
                r -= 1
                c -= 1
                
            answer[r-1][c]=i
            i+=1
 
    return sum(answer, [])