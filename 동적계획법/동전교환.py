"""
여러 단위의 동전들이 주어져 있을때
거스름돈을 가장 적은 수의 동전으로 교환 해주려면 어떻게 주면 되는가?
각 단위의 동전은 무한정 쓸 수 있다.


동전의 종류개수 N(1<=N<=12)
N개의 동전의 종류
거슬러 줄 금액 M(1<=M<=500)
3
1 2 5
15
"""
import sys
input=sys.stdin.readline

n=int(input()) # 동전의 종류개수 (1~12)
arr=list(map(int, input().split())) # 동전의 종류
m=int(input()) # 거슬러 줄 금액 M(1~500)

d=[sys.maxsize]*(m+1) # dp[i]= i원을 거슬러 줄 동전의 최소개수
d[0]=0

for i in range(n):
    for j in range(arr[i],m+1):
        d[j]=min(d[j], d[j-arr[i]]+1)
print(d[m])
