"""
이진수
0으로 시작하지않음
1이 두번 연속으로 나타나지 않음. 11을 부분 문자열로 갖지않음

이친수 : 1, 10, 100, 101, 1000, 1001
이친수X : 0010101, 101101

N(1~90)자리의 이친수의 개수 구하기]
"""

import sys
input=sys.stdin.readline

n=int(input())

d=[[0 for i in range(2)] for j in range(n+1)]
d[0][0]=0 # 이친수는 0으로 시작하지 않음
d[1][1]=1 # 1은 이친수

for i in range(2, n+1):
    d[i][0]=d[i-1][0]+d[i-1][1]
    d[i][1]=d[i-1][0]

print(d[n][0]+d[n][1])