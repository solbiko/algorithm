"""
N개의 문제, 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩니다.
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다.

첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.
5 20
10 5
25 12
15 8
6 3
7 4

제한 시간안에 얻을 수 있는 최대 점수를 출력
"""

# 문제의 개수,제한 시간
n,m=map(int, input().split())

arr=[]
visited=[False]*(n+1)# 문제 점수, 시간


for _ in range(n):
    s,t=map(int, input().split())
    arr.append((s,t))
# print(arr)

maxScore=0
def dfs(idx, score, time): # DFS
    # 문제 인덱스, 점수, 시간
    global maxScore
    if time>m:
        return
    if idx==n:
        maxScore=max(score,maxScore)
    else:
        dfs(idx+1, score+arr[idx][0], time+arr[idx][1]) # 현재문제를 푸는 경우
        dfs(idx+1, score, time) # 현재문제 풀지않고 다음 문제로 넘어감

dfs(0,0,0)
print(maxScore)