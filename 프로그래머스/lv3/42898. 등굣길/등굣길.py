def solution(m, n, puddles):
    
    d = [[0]*(m+1) for _ in range(n+1)]
    for i, j in puddles:
        d[j][i] = 1
    
    d[0][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if d[i][j]==1:
                d[i][j] = 0
            else:
                d[i][j] = (d[i-1][j]+d[i][j-1]) % 1000000007
    
    return d[n][m]