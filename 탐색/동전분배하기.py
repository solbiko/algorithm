"""
N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다.
세 명이 받은 각각의 총액을 계산해
총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력
단 세 사람의 총액은 서로 달라야 합니다.

첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다.
그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.
7
8
9
11
12
23
15
17
"""
import sys

n=int(input())
coin=list()
for _ in range(n):
    coin.append(int(input()))
# print(coin)

money=[0]*3 # 세사람의 총액
res=sys.maxsize # 총액이 가장 큰 사람과 가장 작은 사람의 최소차

def dfs(idx):
    global res
    if idx==n:
        subVal=max(money)-min(money) # 총액의 차
        if res>subVal:
            # 총액은 서로 다른지 비교
            tmp=set()
            for i in money:
                tmp.add(i)
            if len(tmp)==3:
                res=subVal

    else:
        for i in range(3): # A,B,C
            money[i]+=coin[idx]
            dfs(idx+1)
            money[i]-=coin[idx]

dfs(0)
print(res)