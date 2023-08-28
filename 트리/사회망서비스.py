"""
사회망 서비스에 속한 사람들은 얼리 아답터이거나 얼리 아답터가 아니다. 얼리 아답터가 아닌 사람들은 자신의 모든 친구들이 얼리 아답터일 때만 이 아이디어를 받아들인다.
가능한 한 최소의 수의 얼리 아답터를 확보

8
1 2
1 3
1 4
2 5
2 6
4 7
4 8

"""
import sys
sys.setrecursionlimit(10 ** 9)

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

