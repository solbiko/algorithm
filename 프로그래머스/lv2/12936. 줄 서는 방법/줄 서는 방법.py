def solution(n, k):
    answer = []
    
    fList = [0] * 21
    fList[0] = 1
    for i in range(1, n+1):
        fList[i] = fList[i-1] * i

    visited = [False] * 21   # 숫자 사용여부 리스트
    s = [0] * (n+1) # 출력 순열 리스트

    for i in range(1, n+1):
        cnt =1
        for j in range(1, n+1):
            if visited[j]:
                continue
            if k <= cnt * fList[n-i]: 
                k -= (cnt-1) * fList[n-i]
                s[i] = j
                visited[j] = True
                break
            cnt += 1

    return s[1:]
