"""
2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값
블록이 추가되는 경우는 없다
이동하려고 하는 쪽의 칸이 먼저 합쳐진다. 예를 들어, 위로 이동시키는 경우에는 위쪽에 있는 블록이 먼저 합쳐지게 된다
3
2 2 2
4 4 4
8 8 8

0 2 4
0 4 8
0 8 16

16
"""
import sys, copy
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

res = 0


def move(dir):
    if dir == 0:  # 위로 밀기
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[idx][j] == 0:  # 비어있으면
                        board[idx][j] = temp
                    elif board[idx][j] == temp:  # 같으면
                        board[idx][j] = temp * 2  # 합체
                        idx += 1
                    else:  # 다르면
                        idx += 1
                        board[idx][j] = temp

    elif dir == 1:  # 아래로 밀기
        for j in range(n):
            idx = n-1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[idx][j] == 0:
                        board[idx][j] = temp
                    elif board[idx][j] == temp:
                        board[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][j] = temp

    elif dir == 2:  # 왼쪽으로 밀기
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = temp

    else:  # 오른쪽으로 밀기
        for i in range(n):
            idx = n-1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[i][idx] = temp


def dfs(cnt):
    global board, res
    if cnt == 5:  # 보드 최댓값 찾기
        return max(map(max, board))


    temp_a = copy.deepcopy(board)
    for i in range(4):  # 네방향으로 밀기
        move(i)
        dfs(cnt+1)
        board = copy.deepcopy(temp_a)

dfs(0)
print(res)