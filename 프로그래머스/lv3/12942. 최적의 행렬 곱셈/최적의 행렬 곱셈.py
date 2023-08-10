import sys
answer = sys.maxsize 

def solution(matrix_sizes):
    
    n= len(matrix_sizes)
    matrix_sizes.insert(0, (0,0))
    
    # 최소 연산 횟수 저장 리스트
    d=[[-1 for j in range(n+1)] for i in range(n+1)]

    def execute(s,e):
        answer = sys.maxsize 

        if d[s][e] != -1: # 이미 계산
            return d[s][e]
        
        if s==e: # 행렬 1개
            return 0
        
        if s+1==e: # 행렬 2개
            return matrix_sizes[s][0] * matrix_sizes[s][1] * matrix_sizes[e][1]

        for i in range(s,e):
            answer=min(answer, matrix_sizes[s][0] * matrix_sizes[i][1] * matrix_sizes[e][1] + execute(s,i) + execute(i+1,e))
            
        d[s][e]=answer
        return d[s][e]

    return execute(1,n)

