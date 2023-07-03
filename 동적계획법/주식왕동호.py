"""
주식 종류와 기간, 초기 자금 등이 주어졌을 때 동호가 최종적으로 가질 수 있는 돈의 최댓값

주식의 개수 C(1 ≤ C ≤ 50)과 주식 매입 및 매각을 할 기간 D(2 ≤ D ≤ 10), 초기 자금 M(1 ≤ M ≤ 200,000)
두 번째 줄부터 C+1번째 줄까지 각 줄에는 각각 주식이 날짜에 따라 변하는 값이 입력
2 3 10
10 15 15
13 11 20
"""
import sys
input=sys.stdin.readline

c,d,m=map(int, input().split())
a=[]
for _ in range(c):
    a.append(list(map(int,input().split())))

for j in range(1,d):  # 날짜
    cache=[0]*(m+1)
    for i in range(c): # 주식
        now=a[i][j]
        pre=a[i][j-1] # 같은주식 전날 값
        for k in range(a[i][j-1],m+1):
            cache[k] = max(cache[k], cache[k-pre]+now-pre)
    m += cache[m]

print(m)




