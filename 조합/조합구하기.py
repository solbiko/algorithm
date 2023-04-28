"""
1~N 번호 구슬, M개 뽑는 방법의 수 출력
N(3<=N<=10)과 M(2<=M<=N)
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
res=[0]*m
total=0

def dfs(x,s):
    global total
    if x==m:
        for i in res:
            print(i, end=" ")
        print()
        total+=1
    else:
        for i in range(s, n+1):
            res[x]=i
            dfs(x+1,i+1)


dfs(0,1)
print(total)