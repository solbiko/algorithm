"""
N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.
"""
import sys
input=sys.stdin.readline

n,m = map(int, input().split())

# 리스트
a=[[0]*(n+1)]
# 합배열
d=[[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    a.append([0]+[int(x) for x in input().split()])

for i in range(1,n+1):
    for j in range(1,n+1):
        d[i][j]=d[i-1][j]+d[i][j-1]-d[i-1][j-1]+a[i][j]

# 질의
for _ in range(m):
    x1,y1,x2,y2=map(int, input().split())
    res=d[x2][y2]-d[x1-1][y2]-d[x2][y1-1]+d[x1-1][y1-1]
    print(res)