from itertools import product
dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]

def solution(clockHands):
    answer = int(1e9)
    n = len(clockHands)

    def calc(r, c):
        temp = 0
        for d in range(5):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                temp += data[nr][nc]
        return (clockHands[r][c] + temp) % 4

    for li in product(range(4), repeat=n):
        data = [[0] * n for _ in range(n)]

        data[0] = list(li)  # 1행
        for i in range(1, n):  # 2~(n-1)행
            for j in range(n):
                data[i][j] = (4 - calc(i - 1, j)) % 4

        for i in range(n):
            if calc(n-1, i) != 0:
                break
        else:
            answer = min(answer, sum([sum(t) for t in data]))

    return answer
