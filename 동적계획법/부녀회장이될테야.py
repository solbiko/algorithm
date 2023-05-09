"""
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로
첫 번째 줄에 정수 k(1 ≤ k),
두 번째 줄에 정수 n(n ≤ 14)
"""
import sys
input=sys.stdin.readline

d=[[0 for j in range(15)] for i in range(15)]
for i in range(1,15):
    d[i][1]=1 # i층의 1호는 항상 1
    d[0][i]=i # 0층의 i호는 i

for i in range(1,15): # 층
    for j in range(2,15): # 호
        d[i][j]=d[i-1][j]+d[i][j-1]

t = int(input())
for _ in range(0, t):
    k=int(input())
    n=int(input())
    print(d[k][n])
