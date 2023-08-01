def solution(rows, columns, queries):
    answer = []
    arr=[[0]*(columns+1) for _ in range(rows+1)]
    
    h=1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            arr[i][j]=h        
            h+=1
    
    for x1, y1, x2, y2 in queries:
        tmp=arr[x1][y1]
        min_val=tmp
        
        for k in range(x1,x2): # 왼쪽으로
            t = arr[k+1][y1]
            arr[k][y1] = t
            min_val = min(min_val, t)

        for k in range(y1,y2): # 아래로
            t = arr[x2][k+1]
            arr[x2][k] = t
            min_val = min(min_val, t)

        for k in range(x2,x1,-1): # 오른쪽으로
            t = arr[k-1][y2]
            arr[k][y2] = t
            min_val = min(min_val, t)

        for k in range(y2,y1,-1): # 위로
            t = arr[x1][k-1]
            arr[x1][k] = t
            min_val = min(min_val, t)

        arr[x1][y1+1] = tmp
        answer.append(min_val)
    
    return answer