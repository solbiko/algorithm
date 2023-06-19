"""
↑ ↑  ↑  ↑   ↑
1 2 ←3 ←4⟶ ←5⟶
  ↓         ↓
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다.
CCTV의 최대 개수는 8개를 넘지 않는다.
첫째 줄에 사각 지대의 최소 크기를 출력한다.

4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
"""
import sys
import copy

input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m=map(int,input().split())
board=[]  # 사무실
cctv=[]
for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

min_value = sys.maxsize  # 사각지대 최소크기

# 네방향
dr=[0,1,0,-1]
dc=[1,0,-1,0]

# cctv 방향
mode = [
    [],
    [[0], [1], [2], [3]],  # 단방향
    [[0, 2], [1, 3]],  # 반대 두방향
    [[0, 1], [1, 2], [2, 3], [0, 3]],  # 90도 두방향
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],  # 90도 세방향
    [[0, 1, 2, 3]],]  # 네방향


def dfs(idx, board):
    global min_value

    # 전체 cctv 탐색완료
    if idx == len(cctv):
        count = 0
        # 사각지대 카운트
        for i in range(n):
            count += board[i].count(0)
        min_value = min(min_value, count)
        return

    board_cp = copy.deepcopy(board)  # 사무실 복사
    cctv_num, x, y = cctv[idx]

    # cctv의 방향에 따라서 탐색
    for i in mode[cctv_num]:
        for j in i:
            nx=x
            ny=y
            # 한 방향 계속 탐색
            while True:
                nx+=dr[j]
                ny+=dc[j]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위를 넘어가면 중단
                    break
                if board_cp[nx][ny] == 6:  # 벽이면 중단
                    break
                elif board_cp[nx][ny] == 0:  # 감시가능
                    board_cp[nx][ny] = '#'

        dfs(idx+1, board_cp)
        board_cp = copy.deepcopy(board)  # 보드 초기화


dfs(0, board)
print(min_value)
