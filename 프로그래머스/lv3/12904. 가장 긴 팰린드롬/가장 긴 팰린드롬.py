def solution(s):
    answer = 0
    
    def isPalindrome(x):
        if x==x[::-1]:
            return True
    
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPalindrome(s[i:j]):
                answer=max(answer, len(s[i:j]))
    
    return answer