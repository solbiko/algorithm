"""
유람선에는 N명의 승객이 타고 있습니다.
구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있으며,
보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력

첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다. 각 승객의 몸무게는 M을 넘지는 않습니다.
5 140
90 50 70 100 60
"""
from collections import deque

n,m=map(int, input().split())
p=list(map(int,input().split()))
p.sort()
p=deque(p)

cnt=0
while p:
    if len(p)==1: # 마지막 한명 남으면
        cnt+=1
        break

    if p[0]+p[-1]>m: # 맨앞사람과 맨뒷사람 같이 못탐
        p.pop() # 무거운 사람만 태우고 나감 pop
        cnt+=1
    else: # 맨앞사람 맨뒷사람 둘 다 탐
        p.pop()
        p.popleft()
        cnt+=1
print(cnt)
