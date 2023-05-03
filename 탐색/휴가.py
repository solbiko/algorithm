"""
N+1일째 되는 날 휴가, 남은 N일 동안 최대한 많은 상담
상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P
휴가를 가기 위해 얻을 수 있는 최대 수익

첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 1일부터 N일까지 순서대로 주어진다. (1 ≤ T ≤ 7, 1 ≤ P ≤ 100)

7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
"""
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    t,p=map(int, input().split())
    arr.append((t,p))
arr.insert(0,(0,0)) # 1부터 시작
# print(arr)

maxP=0
def dfs(idx, price):
    global maxP
    if idx==n+1: # 다음날에 종료
        maxP=max(price,maxP)
    else:
        if idx+arr[idx][0]<=n+1: # 하는경우
            dfs(idx+arr[idx][0], price+arr[idx][1])
        dfs(idx+1, price) # 안하는 경우

dfs(1,0)
print(maxP)