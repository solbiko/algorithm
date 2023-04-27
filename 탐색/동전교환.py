"""
여러 단위의 동전들이 주어져 있을때
거스름돈을 가장 적은 수의 동전으로 교환 해주려면 어떻게 주면 되는가?
각 단위의 동전은 무한정 쓸 수 있다.


동전의 종류개수 N(1<=N<=12)
N개의 동전의 종류
거슬러 줄 금액 M(1<=M<=500)
"""
import sys
input=sys.stdin.readline

n=int(input()) # 동전의 종류개수 (1~12)
arr=list(map(int, input().split())) # 동전의 종류
arr.sort(reverse=True)
m=int(input()) # 거슬러 줄 금액 M(1~500)

res=sys.maxsize # 거슬러 줄 동전의 최소개수

def dfs(x, sum):
    global res
    # x: 동전의 사용개수, sum : 동전 합계
    if sum>m:
        return
    if sum==m:
        res= min(res, x)
    for i in (arr):
        dfs(x+1, sum+i)

dfs(0,0)

print(res)