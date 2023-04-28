"""
가장 윗줄에 1부터 N까지의 숫자, 둘째 줄부터 위의 두개를 더한 값이 저장
N: 4, 가장윗줄: 3 1 2 4
 3 1 2 4
  4 3 6
   7 9
   16

N(1~10)과 가장 밑에 있는 숫자(F)가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하기
답이 존재 하지 않는 경우는 입력으로 주어지지 않는다

"""
import sys
input=sys.stdin.readline

n,f=map(int,input().split())
visited=[False]*(n+1)
p=[0]*n

# 이항계수
b=[1]*n
for i in range(1,n):
    b[i]=b[i-1]*(n-i)//i

def dfs(x, sum):
    global visited
    if x==n and sum==f:
        for i in p:
            print(i, end=" ")
        print()
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                p[x] = i
                dfs(x+1, sum+(p[x]*b[x]))
                visited[i] = False
dfs(0,0)