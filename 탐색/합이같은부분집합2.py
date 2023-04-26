"""
N개의 원소로 구성된 자연수 집합
이 집합을 두 개의 부분집합으로 나누었을 때 두 부분집합의 원소의 합이 서로 같은 경우
{1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10}
"""
import sys
input=sys.stdin.readline

n=int(input())
list = list(map(int, input().split()))
total=sum(list)

def dfs(idx, sum):
    if sum>(total-sum)//2: # sum이 홀수인 경우가 있기 때문에 > 체크
        return
    if idx==n:
        if sum==(total-sum):
            print("yes")
            sys.exit(0)
    else:
        dfs(idx+1, sum+list[idx])
        dfs(idx+1, sum)

dfs(0,0)
print("NO")

