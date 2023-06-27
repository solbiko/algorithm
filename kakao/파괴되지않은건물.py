"""
1 ≤ board의 행의 길이 (= N) ≤ 1,000
1 ≤ board의 열의 길이 (= M) ≤ 1,000
1 ≤ skill의 행의 길이 ≤ 250,000

"""
def solution(board, skill):

    answer = 0  # 적의 공격 혹은 아군의 회복 스킬이 모두 끝난 뒤 파괴되지 않은 건물의 개수
    n = len(board)
    m = len(board[0])
    temp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for t, r1, c1, r2, c2, d in skill:
        tt = -d if t == 1 else d
        temp[r1][c1] += tt
        temp[r1][c2 + 1] -= tt
        temp[r2 + 1][c1] -= tt
        temp[r2 + 1][c2 + 1] += tt

    # 행 기준 누적합
    for i in range(n):
        for j in range(m):
            temp[i][j + 1] += temp[i][j]

    # 열 기준 누적합
    for j in range(m):
        for i in range(n):
            temp[i + 1][j] += temp[i][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
         [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))