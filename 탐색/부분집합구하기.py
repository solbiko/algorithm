"""
1부터 자연수 N(1~10)
부분집합을 모두 출력하는 프로그램 을 작성
"""
import sys
input=sys.stdin.readline

n=int(input())

def dfs(v):
    if v==n+1:
        for i in range(1,n+1):
            if ch[i]==1:
                print(i, end='')
        print()
    else:
        ch[v]=1
        dfs(v+1)
        ch[v]=0
        dfs(v+1)

ch=[0]*(n+1)
dfs(1)