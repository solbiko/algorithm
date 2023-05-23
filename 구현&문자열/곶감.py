"""
마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다.

격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경
회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 회전
행번호, 방향 0왼쪽/1오른쪽, 회전 격자 수

M개의 회전명령을 실행하고 난 후 모래시계 모양의 영역의 감 총 개수 출력

N(3<=N<=20),N 홀수
N줄에 걸쳐 각 줄에 N개의 자연수(각 격자안에 있는 감의 개수, ~100)
회전명령의 개수인 M(1<=M<=10)
M개의 회전명령 정보

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4
"""
import sys
input=sys.stdin.readline

# 격자판
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

# 회전 명령
m=int(input())
for _ in range(m):
    # 행, 방향, 개수
    r,d,c=map(int,input().split())

    if d==0: # 왼쪽
        for i in range(c):
            a[r-1].append(a[r-1].pop(0)) # 첫번째 값 맨뒤에 추가
    elif d==1: # 오른쪽
        for i in range(c):
            a[r - 1].insert(0,(a[r - 1].pop())) # 마지막 값 0에 삽입

# 모래시계 모양 영역 총 감개수 출력
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)