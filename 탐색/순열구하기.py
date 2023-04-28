"""
1~N번호 구슬
M개를 뽑아 일렬로 나열하는 방법 출력
N(3~10), M(2<=M<=N)
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
visited=[False]*(n+1)
res=[0]*m
total=0

def dfs(x):
    global total
    global visited
    if x==m:
        for i in res:
            print(i, end=" ")
        print()
        total+=1
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i]=True
                res[x]=i
                dfs(x+1)
                visited[i]=False


dfs(0)
print(total)