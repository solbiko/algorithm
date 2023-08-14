INF=float('inf')
def solution(alp, cop, problems):
    max_alp=0 # 알고력
    max_cop=0 # 코딩력
    for a,b,c,d,e in problems:
        max_alp=max(max_alp, a)
        max_cop=max(max_cop, b)
            
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    # dp[i][j] : 알고력이 i, 코딩력이 j를 얻기위해 걸리는 최소시간
    dp = [[INF]*(max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop]=0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            
            # 코딩공부(1시간)로 높이기
            if i != max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j != max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
                
            # 문제 풀어서 높이기
            for nalp, ncop, ralp, rcop, cost in problems: # [필요알고력, 필요코딩력, 증가알고력, 증가코딩력, 문제푸는데드는시간]
                if i >= nalp and j >= ncop:
                    next_alp = min(max_alp, i+ralp)
                    next_cop = min(max_cop, j+rcop)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j]+cost)
                    
    return dp[-1][-1]  # 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간

        
        
    
    
    
    
    
    
    
    return answer