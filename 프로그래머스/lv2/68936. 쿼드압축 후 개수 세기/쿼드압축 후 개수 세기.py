def solution(arr):
    answer = [0, 0]

    def quad(r,c,n):
        
        if len(arr) == 1:
            answer[arr[r][c]] += 1
            return
        else:
            tg = arr[r][c]
            
        for i in range(n):
            for j in range(n):
                if arr[r+i][c+j] != tg:
                    n=n//2
                    quad(r, c, n)
                    quad(r, c+n, n)
                    quad(r+n, c, n)
                    quad(r+n, c+n, n)
                    return
        answer[tg] += 1
    
    quad(0, 0, len(arr))
    
    return answer
