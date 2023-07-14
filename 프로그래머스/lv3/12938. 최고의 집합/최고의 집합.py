def solution(n, s):
    answer = []
    if n>s:
        return [-1]
    
    answer=[s//n]*n
    for i in range(s%n):
        answer[-i-1]+=1
    return answer