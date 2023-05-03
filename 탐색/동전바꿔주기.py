"""
k가지 동전이 각각 n1, n2, ... , nk개
T원의 지폐를 동전으로 바꿔 주려고한다

입력으로 지폐의 금액 T, 동전의 가지수 k, 각 동전 하나의금액 pi와 개수 ni가 주어질 때 (i=1,2,...,k)
지폐를 동전으로 교환하는 방법의 가지 수

첫째 줄에는 지폐의 금액 T(0<T≤10,000),
둘째 줄에는 동전의 가지 수k(0<k≤10),
셋째 줄부터 마지막 줄까지는 각 줄에 동전의금액 pi(0<pi≤T)와 개수 ni(0<ni≤10)가 주어진다.

20
3
5 3
10 2
1 5
"""
import sys
input=sys.stdin.readline

t=int(input()) # 지폐금액
k=int(input()) # 동전가지수
coin=list()
for i in range(k):
    pi,ni=map(int, input().split())
    coin.append((pi,ni))


cnt=0 # 지폐를 동전으로 교환하는 방법의 가지 수
def dfs(idx, sum):
    global cnt
    if idx==k:
        if sum==t:
            cnt+=1
    else:
        for i in range(coin[idx][1]+1): # 0~ni
            dfs(idx+1, sum+coin[idx][0]*i) # sum+ pi*(0~ni)

dfs(0,0)
print(cnt)
