def solution(board):
    x = sum(row.count('X') for row in board)
    o = sum(row.count('O') for row in board)

    
    def check_win(t):
        # Check rows
        for i in range(3):
            if all(j==t for j in board[i]):
                return True

        # Check columns
        for i in range(3):
            if all(board[j][i] == t for j in range(3)):
                return True

        # Check diagonals
        if all(board[i][i] == t for i in range(3)):
            return True
        if all(board[i][2-i] == t for i in range(3)):
            return True

        return False
    
    
    if x-o>0 or abs(x-o)>1:
        return 0
    elif (check_win('O') and x==o) or (check_win('X') and x!=o):
        return 0

    return 1