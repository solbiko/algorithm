"""
지도 정보가 N*N(1~50) 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다.
각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.

격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
"""
import sys
input=sys.stdin.readline

# 격자판
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)

cnt=0

# 네 방향 탐색을 위한 상수
dr=[0,1,0,-1]
dc=[1,0,-1,0]

for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dr[k]][j+dc[k]] for k in range(4)):
            cnt+=1

print(cnt)


