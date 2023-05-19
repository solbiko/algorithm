"""
각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩니다.
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다.

첫 번째 줄에 문제의 개수N(1<=N<=100)과 제한 시간 M(10<=M<=1000)이 주어집니다.
두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.
5 20
10 5
25 12
15 8
6 3
7 4

제한 시간안에 얻을 수 있는 최대 점수를 출력
"""
import sys
input=sys.stdin.readline

# 문제의 개수,제한 시간
n,m=map(int, input().split())
d= [0]*(m+1)

for _ in range(n):
    pv,pt=map(int, input().split())
    for i in range(m, pt-1, -1): # 뒤에서부터 1개 쓸 수 있는 시간까지
        d[i]=max(d[i], d[i-pt]+pv)

print(d[m])