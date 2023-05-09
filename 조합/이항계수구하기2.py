import sys
input=sys.stdin.readline

n,k=map(int,input().split())
d=[[0 for j in range(n+1)] for i in range(n+1)] # dp 테이블

for i in range(0, n+1):
    d[i][1]=i # i개 중에 1개를 뽑는 경우의 수 i
    d[i][0]=1 # i개 중 1개도 선택하지 않는 경우의 수 1
    d[i][i]=1 # i개 중에 i개를 선택하는 경우의 수 1개


for i in range(2, n+1):
    for j in range(1,i): # 고르는 수의 개수가 전체 개수를 넘을 수 없음
        d[i][j]=d[i-1][j]+d[i-1][j-1] # 조합 점화식
        d[i][j]=d[i][j]%10007

print(d[n][k])