dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
n = m = 0

visited = [[0] * 5 for _ in range(5)]  # 방문
block = [[0] * 5 for _ in range(5)]  # 발판


def dfs(p1, p2):
    global visited, block

    r, c = p1[0], p1[1]  # 현재 플레이어 좌표
    opr, opc = p2[0], p2[1]  # 상대 플레이어 좌표

    if visited[r][c]:
        return 0

    ret = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m or visited[nr][nc] or block[nr][nc] == 0:
            continue

        visited[r][c] = 1
        val = dfs([opr, opc], [nr, nc]) + 1
        visited[r][c] = 0

        if ret % 2 == 0 and val % 2 == 1:  # 현재 저장된 턴은 패배, 새로 계산된 턴 승리
            ret = val
        elif ret % 2 == 0 and val % 2 == 0:  # 현재 저장된 턴은 패배, 새로 계산된 턴 패배
            ret = max(ret, val)
        elif ret % 2 == 1 and val % 2 == 1:  # 현재 저장된 턴은 승리, 새로 계산된 턴 승리
            ret = min(ret, val)
    return ret


def solution(board, aloc, bloc):
    global n, m
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            block[i][j] = board[i][j]

    return dfs(aloc, bloc)

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2]))
# print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]],	[1, 0],	[1, 2]))
# print(solution([[1, 1, 1, 1, 1]], [0, 0],	[0, 4]))
