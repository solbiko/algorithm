import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=list(map(int, input().split()))
m=int(input())

def dfs(x,s,sum):
    global cnt
    if x==k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s,n):
            dfs(x+1,i+1,sum+arr[i])

cnt=0
dfs(0,0,0)
print(cnt)