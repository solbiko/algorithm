def solution(arr):
    answer = [0, 0]

    def quad(arr,r,c,n):
        tg = arr[r][c]
        for i in range(n):
            for j in range(n):
                if arr[r+i][c+j] != tg:
                    n=n//2
                    quad(arr, r, c, n)
                    quad(arr, r, c+n, n)
                    quad(arr, r+n, c, n)
                    quad(arr, r+n, c+n, n)
                    return
        answer[tg] += 1
    
    quad(arr, 0, 0, len(arr))
    
    return answer
