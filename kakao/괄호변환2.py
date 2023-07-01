"""
p는 '(' 와 ')' 로만 이루어진 문자열이며 길이는 2 이상 1,000 이하인 짝수입니다.
문자열 p를 이루는 '(' 와 ')' 의 개수는 항상 같습니다.
"""
def solution(p):
    if p=='': # 1
        return p

    r=True
    c=0
    for i in range(len(p)): # 2
        if p[i]=='(':
            c-=1
        else:
            c+=1

        if c>0: # 순서 올바르지않음
            r=False

        if c==0:
            if r: # 3
                return p[:i+1]+solution(p[i+1:])
            else: # 4
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
