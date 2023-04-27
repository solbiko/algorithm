import sys
input=sys.stdin.readline

# 트럭허용무게, 바둑이 수
c,n=map(int, input().split())
# 바둑이 무게
arr=[0]*n
for i in range(n):
    arr[i]=int(input())

maxVal=0
def dfs(idx, sum):
    global maxVal
    if sum>c:
        return
    if idx==n:
        if maxVal<sum:
            maxVal=sum
    else:
        dfs(idx+1, sum) # 더하지 않는 경우
        dfs(idx+1, sum+arr[idx])  # 더하는 경우



dfs(0,0)
print(maxVal)