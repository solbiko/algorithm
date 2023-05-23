"""
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력
첫 줄에 자연수 N이 주어진다.(1<=N<=50)

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

155
"""
import sys
input=sys.stdin.readline

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

res=0

cross1 = 0  # 대각선
cross2 = 0  # 대각선

for i in range(n):
    # 대각선
    cross1+=a[i][i]
    cross2+=a[-1-i][-1-i]

    sum1=0 # 행
    sum2=0 # 열
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>res:
        res=sum1
    if sum2>res:
        res=sum2
        
if cross1 > res:
    res=cross1
if cross2 > res:
    res=cross2
print(res)


