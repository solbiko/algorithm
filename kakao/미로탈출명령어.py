"""
  격자의 크기를 뜻하는 정수 n, m,
  출발 위치를 뜻하는 정수 x, y,
  탈출 지점을 뜻하는 정수 r, c,
  탈출까지 이동해야 하는 거리를 뜻하는 정수 k
  """


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 왼쪽, 아래, 위, 오른쪽
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dAlpha = ['d', 'l', 'r', 'u']
answer = "z"


def isVaild(nx, ny, n, m): # 미로 격자 체크
    return 1 <= nx and nx <= n and 1 <= ny and ny <= m


def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    global answer
    # print("prev_s", prev_s, "cnt", cnt, "answer", answer)

    if k < cnt + abs(x - r) + abs(y - c):
        print("prev_s", prev_s, "cnt", cnt, "answer", answer)
        print(cnt + abs(x - r) + abs(y - c))
        # return

    # 도착
    if x == r and y == c and cnt == k:
        answer = prev_s
        return

    for i in range(4):

        if isVaild(x + dx[i], y + dy[i], n, m) and prev_s < answer:

            dfs(n, m, x + dx[i], y + dy[i], r, c, prev_s+dAlpha[i], cnt+1, k)


def solution(n, m, x, y, r, c, k):

    # 탈출 최단 거리
    dist = abs(x - r) + abs(y - c)

    # 탈출 도착 후, 2n 이동하면 제자리
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    dfs(n, m, x, y, r, c, "", 0, k)

    return answer

print(solution(3,4,2,3,3,1,5)) # "dllrl"
print(solution(2,2,1,1,2,2,2)) # "dr"
print(solution(3,3,1,2,3,3,4)) # "impossible"
