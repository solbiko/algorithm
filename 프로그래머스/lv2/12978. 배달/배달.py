import sys
def solution(N, road, K):
    answer = 0

    d = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]
    for i in range(1, N+1):
        d[i][i] = 0
        
    g=[[]*(N+1) for _ in range(N+1)]
    for s,e,w in road:
         if d[s][e]>w:
            d[s][e]=w
         if d[e][s]>w:
            d[e][s]=w

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                d[i][j]=min(d[i][k]+d[k][j], d[i][j])
    
    for i in range(N+1):
        if d[1][i]<=K:
            answer+=1
            
    return answer