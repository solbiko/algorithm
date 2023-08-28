import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n=int(input())

g=[[] for _ in range(n+1)]
for _ in range(n-1):
    s,e=map(int, input().split())
    g[s].append(e)
    g[e].append(s)

dp=[[0,0] for _ in range(n+1)]
visited=[False]*(n+1)

def dfs(x):
    visited[x]=True
    dp[x][1]=1

    for i in g[x]:
        if not visited[i]:
            dfs(i)

            dp[x][0]+=dp[i][1]
            dp[x][1]+=min(dp[i][0], dp[i][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))