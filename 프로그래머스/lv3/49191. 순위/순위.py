def solution(n, results):
    answer = 0

    board = [[0] * (n + 1) for _ in range(n + 1)]

    for a, b in results:
        board[a][b]=1
        board[b][a]=-1


    for k in range(1, n + 1):
        for s in range(1, n + 1):
            for e in range(1, n + 1):
                if board[s][k] == board[k][e] == 1:
                    board[s][e] = 1 # 이김
                    board[e][s] = board[k][s] = board[e][k] = -1 # 짐
    
    for row in board:
        if row[1:].count(0) == 1: # 1 승리 /0 모름 / -1짐
            answer += 1
            
    return answer
