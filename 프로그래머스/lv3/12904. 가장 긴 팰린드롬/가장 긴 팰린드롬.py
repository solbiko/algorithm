def solution(s):
    answer = 0

    if s == s[::-1]:
        return len(s)

    def pail(i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return len(s[i+1:j])
    
    for i in range(len(s)):
        answer = max(answer, pail(i, i+1), pail(i, i+2))

    return answer