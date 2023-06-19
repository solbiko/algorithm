"""
가장 위, 왼쪽부터 붙임
자리없으면 시계방향으로 90도 회전
0도, 90도, 180도, 270도 회전해도 없으면 버림

노트북 세로, 가로 N,M(1 ≤ M ≤ 40), 스티커 개수 K(1 ≤ K ≤ 100)
i번째 스티커가 인쇄된 모눈종이의 행의 개수와 열의 개수를 나타내는 Ri(1 ≤ Ri ≤ 10)와 Ci(1 ≤ Ci ≤ 10)
Ri개의 줄에는 각 줄마다 모눈종이의 각 행을 나타내는 Ci개의 정수가 한 개

5 4 4
3 3
1 0 1
1 1 1
1 0 1
2 5
1 1 1 1 1
0 0 0 1 0
2 3
1 1 1
1 0 1
3 3
1 0 0
1 1 1
1 0 0

첫째 줄에 주어진 스티커들을 차례대로 붙였을 때 노트북에서 스티커가 붙은 칸의 수를 출력
"""
import sys
import copy

input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m,k=map(int, input().split())
board=[[0]*m for _ in range(n)]
stickers=[]
for _ in range(k):
    x,y=map(int, input().split())
    tmp=[]
    for _ in range(x):
        tmp.append(list(map(int,input().split())))
    stickers.append(tmp)

# 네방향
dr=[0,1,0,-1]
dc=[1,0,-1,0]


# 스티커 90도 회전
def rotate(sticker):
    c, r = len(sticker), len(sticker[0])
    temp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            temp[i][j] = sticker[c-1-j][i]
    return temp

# 붙이기 체크
def check(sticker, y, x):
    r, c = len(sticker), len(sticker[0])

    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and board[y+i][x+j] == 1:  # 이미 붙어있는 경우
                return False

    # 붙이기
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                board[y+i][x+j] = 1
    return True

for s in stickers:
    direction = 1  # 스티커 방향 (회전여부)
    while True:
        flag = False
        r, c = len(s), len(s[0])  # 스티커 길이
        for y in range(n-(r-1)):
            for x in range(m-(c-1)):
                if check(s,y,x):  # 붙일수있다면
                    flag = True
                    break
            if flag:  # 붙였다면 다음 스티커로
                break
        if not flag:
            if direction==0:  # 네번(360도) 돌렸으면
                break
            s = rotate(s)  # 스티커 돌리기
            direction=(direction+1)%4  # 방향 돌린
        elif flag:
            break

# print(board)

cnt=0
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            cnt+=1

print(cnt)