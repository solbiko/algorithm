def solution(beginning, target):
    n = len(target)
    m = len(target[0])
    
    diff = [[beginning[i][j] ^ target[i][j] for j in range(m)] for i in range(n)]

    sumr = 0
    for i in range(1,n):
        if (diff[i] != diff[0]):
            sumr+=1 # 행 뒤집는 횟수
            if list(map(lambda x: x ^ 1, diff[i])) != diff[0]:
                return -1

    sumc= sum(diff[0]) # 열 뒤집는 횟수

    return min(sumr+sumc, (n-sumr)+(m-sumc))
