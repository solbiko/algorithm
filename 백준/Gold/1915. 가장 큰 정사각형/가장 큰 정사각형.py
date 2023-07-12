import sys
input=sys.stdin.readline

n,m=list(map(int, input().split()))
d=[[0 for j in range(1001)] for i in range(1001)]
max=0 # 변의 길이

for i in range(0,n): # 세로
    arr=list(input())
    for j in range(0,m): # 가로
        d[i][j]=int(arr[j])
        if d[i][j]==1 and j>0 and i>0:
            d[i][j]=min(d[i-1][j-1], d[i][j-1], d[i-1][j]) + 1 #  ︎↖ ← ↑︎ 전부 1이면 +1︎
        if max < d[i][j]:
            max = d[i][j]

print(max*max)