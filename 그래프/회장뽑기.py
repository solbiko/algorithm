"""
회원사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 서로 모두 알 수 있 다.
각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.
예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다.
어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나, 친구의 친구임을 말한다.
또한, 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친국의 친구의 친구임을 말한다.
4점, 5점등은 같은 방법으로 정해진다.

회장의 점수와 회장이 될 수 있는 모든 사람

입력의 첫째 줄에는 회원의 수가 있다. 단, 회원의 수는 50명을 넘지 않는다.
둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다.
회원번호는 1부터 회원의 수만큼 번호가 붙어있다. 마지막 줄에는 -1이 두 개 들어있다
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1

첫째 줄은 회장 후보의 점수와 회장후보 수를 출력하고
두 번째 줄은 회장 후보를 모두 출력 한다.
2 3
2 3 4
"""
import sys
input=sys.stdin.readline

# 회원수
n=int(input())

# 인접행렬
d = array = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]
for i in range(n):
    d[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a==-1 and b==-1:
        break
    d[a][b] = 1
    d[b][a] = 1


for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if d[s][e] > d[s][k] + d[k][e]:
                d[s][e] = min(d[s][e], d[s][k]+d[k][e])

# print(d)

res=[0]*(n+1) # 각 회원의 최대점수
score=sys.maxsize # 최소 점수
for i in range(1,n+1):
    for j in range(1,n+1):
        res[i]= max(res[i], d[i][j])
    score=min(res[i], score)

out=[] # 최소점수의 회원
for i in range(1, n+1):
    if res[i]==score:
        out.append(i)

print(score, len(out))
for x in out:
    print(x, end=" ")