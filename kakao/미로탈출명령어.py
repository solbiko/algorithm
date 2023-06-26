"""
격자의 크기를 뜻하는 정수 n, m,
출발 위치를 뜻하는 정수 x, y,
탈출 지점을 뜻하는 정수 r, c,
탈출까지 이동해야 하는 거리를 뜻하는 정수 k

미로를 탈출하기 위한 경로를 return
미로를 탈출할 수 없는 경우 "impossible"
"""


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dAlpha = ['d', 'l', 'r', 'u']
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

answer = "z"


def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    global answer

    if k-cnt < abs(x-r)+abs(y-c):  # 탈출이동거리 넘는경우
        return

    if x==r and y==c and cnt==k:  # 도착
        answer = prev_s
        return

    for i in range(4):
        nextX=x+dx[i]
        nextY=y+dy[i]
        if 1<=nextX<=n and 1<=nextY<=m and prev_s < answer:  # 격자판, 문자열이 사전순 큰경우
            dfs(n, m, nextX, nextY, r, c, prev_s+dAlpha[i], cnt+1, k)



def solution(n, m, x, y, r, c, k):
    dist = abs(x-r) + abs(y-c)  # 탈출 최단 거리
    if dist>k or (k-dist)%2==1:  # 탈출 도착 후, 2n 이동하면 제자리
        return "impossible"

    dfs(n, m, x, y, r, c, "", 0, k)
    return answer

print(solution(3,4,2,3,3,1,5)) # "dllrl"
print(solution(2,2,1,1,2,2,2)) # "dr"
print(solution(3,3,1,2,3,3,4)) # "impossible"