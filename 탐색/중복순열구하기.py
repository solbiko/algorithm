"""
1부터 N까지 번호가 적힌 구슬
이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력

N(3<=N<=10), M(2<=M<=N)
맨 마지막 총 경우의 수를 출력
"""
import sys
input=sys.stdin.readline
n,m=map(int, input().split())
res=[0]*n
total=0

def dfs(x):
    global total
    if x==m:
        for j in range(m):
            print(res[j], end=' ')
        total+=1
        print()
    else:
        for i in range(1,n+1):
            res[x]=i
            dfs(x+1)

dfs(0)
print(total)