"""
그의 트럭은 C킬로그램 넘게 태 울수가 없다.
철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면,
철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램

C(1<=C<=100,000,000)와 N(1<=N<=30)
259 5
81
58
42
33
61
"""
import sys
input=sys.stdin.readline

# 트럭허용무게, 바둑이 수
c,n=map(int, input().split())
# 바둑이 무게
arr=[]
for _ in range(n):
    arr.append(int(input()))

maxVal=0
def dfs(idx, sum):
    global maxVal

    if idx==n:
        return
    else:
        dfs(idx+1, sum) # 더하지 않는 경우
        dfs(idx+1, sum+arr[idx])  # 더하는 경우

        if sum+arr[idx]>c:
            maxVal=max(maxVal, sum)
        else:
            maxVal=max(maxVal, sum+arr[idx])

dfs(0,0)
print(maxVal)