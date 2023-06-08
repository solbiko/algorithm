"""
칵테일에 들어가는 재료 N개는 공개되어 있다.
재료 쌍 N-1개의 비율을 알아냈고, 이 비율을 이용해서 칵테일에 들어가는 전체 재료의 비율을 알아낼 수 있다.
총 재료 쌍 N-1개의 비율이 입력으로 주어진다. 이때, 칵테일을 만드는데 필요한 각 재료의 양을 구하는 프로그램을 작성하시오.

이때, 필요한 재료의 질량을 모두 더한 값이 최소가 되어야 한다.
칵테일을 만드는 재료의 양은 정수이고, 총 질량은 0보다 커야한다.
a b p q : a번 재료의 질량을 b번 재료의 질량으로 나눈 값이 p/q라는 뜻이다.

만드는데 필요한 재료의 개수 N이 주어지며, N은 10보다 작거나 같은 자연수이다.
N-1개의 줄에는 재료 쌍의 비율이 한 줄에 하나씩 주어지는데, 문제 설명에 나온 형식인 "a b p q"로 주어진다.
재료는 0번부터 N-1까지이며, a와 b는 모두 N-1보다 작거나 같은 음이 아닌 정수이다. p와 q는 9보다 작거나 같은 자연수이다.
5
4 0 1 1
4 1 3 1
4 2 5 1
4 3 7 1
"""
import math
import sys
input=sys.stdin.readline

n=int(input())  # 재료개수
A=[[] for _ in range(n)]  # 비율 리스트
visitList = [False]*n  # 방문체크
amount=[0]*n  # 각 재료의 양
lcm=1  # 최소공배수

# 깊이우선 탐색
def dfs(v):
    visitList[v] = True
    for i in A[v]:
        next=i[0]
        if not visitList[next]:
            amount[next]=amount[v]*i[2]//i[1]  #  * p/q
            dfs(next)

for _ in range(n-1):
    a,b,p,q=map(int, input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))
    lcm*=(p*q)//math.gcd(p,q)

amount[0]=lcm
dfs(0)

# 최대 공약수 계산
mgcd=amount[0]
for i in range(1,n):
    mgcd=math.gcd(mgcd, amount[i])

for i in range(n):
    print(int(amount[i]/mgcd), end=' ')