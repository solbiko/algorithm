def solution(s):
    for i in range(len(s),0,-1): # 문자열 길이 긴 것 부터
        for j in range(len(s)-i+1): # 문자열 시작 인덱스
            if s[j:j+i] == s[j:j+i][::-1]:  
                return i