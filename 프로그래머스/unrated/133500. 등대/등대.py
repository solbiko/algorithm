import sys
sys.setrecursionlimit(10 ** 9)

def solution(n, lighthouse):
    answer = 0
    
    # 인접리스트
    g=[[] for _ in range(n+1)]
    for s,e in lighthouse:
        g[s].append(e)
        g[e].append(s)
    
    dp=[[0,0] for _ in range(n+1)] # [안켠 경우 최적해, 켠 경우 최적해]
    visited=[False]*(n+1)

    def dfs(x):
        visited[x]=True
        dp[x][1]=1
        
        for i in g[x]:
            if not visited[i]:
                dfs(i) # 자식노드방문
                
                dp[x][0]+=dp[i][1] # 안켠경우 자식노드 켜야함
                dp[x][1]+=min(dp[i][0], dp[i][1]) # 켠경우 최소값
    
    dfs(1)
    answer=min(dp[1][0], dp[1][1])
    
    return answer