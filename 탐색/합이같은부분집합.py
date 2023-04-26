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
ch = [0] * (n + 1)
result="NO"

def dfs(idx):
    global result
    arr=[]
    if idx==n+1 :
        sum=0
        for i in range(n):
            if ch[i] == 1:
                sum+=list[i]
        if sum==(total-sum):
            result="YES"
    else:
        ch[idx-1] = 1
        dfs(idx+1)
        ch[idx-1] = 0
        dfs(idx+1)

dfs(0)


print(result)