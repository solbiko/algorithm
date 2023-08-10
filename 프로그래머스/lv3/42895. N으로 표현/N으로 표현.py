def solution(N, number):
    if number == 1:
        return 1
    
    arr = []
    for i in range(1, 10): # 1개부터 8개까지 확인
        s = set()
        s.add(int(str(N)*i)) # 이어붙이는경우
        
        for j in range(i-1): # (1, n-1)부터 (n-1, 1)까지 사칙연산
            for k1 in arr[j]:
                for k2 in arr[-j-1]:
                    s.add(k1+k2)
                    s.add(k1*k2)
                    s.add(k1-k2)
                    if k2!=0: s.add(k1/k2)
                        
        # 만든 집합에 number가 처음 나오는지 확인
        if number in s:
            return i
        arr.append(s)
    
    return -1