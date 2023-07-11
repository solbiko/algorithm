def solution(s):
    answer = 0
    n=len(s)
    pair={'(':')', '{':'}','[':']'}
    
    for i in range(n):
        stack=[]
        flag=True
        for j in range(n):
            tmp=s[(i+j)%n]
            if tmp in ['[','{','(']:
                stack.append(tmp)
            elif stack and pair[stack[-1]]==tmp:
                stack.pop()
            else:
                flag=False
            
        if not stack and flag:
            answer+=1
        
    
    return answer