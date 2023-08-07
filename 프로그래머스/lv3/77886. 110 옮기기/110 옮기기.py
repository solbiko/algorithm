def solution(s):
    answer = []
    
    for x in s: 
        
        # 110 개수 구하기
        stack=[]
        cnt=0
        for i in x:
            if len(stack)>1 and i=='0' and stack[-2]=='1' and stack[-1]=='1':
                stack.pop()
                stack.pop()
                cnt+=1
            else:
                stack.append(i)

        idx=0
        for s in stack[::-1]:
            if s == '0':
                break
            else:
                idx+=1
        answer.append(''.join(stack[:len(stack)-idx]) + '110'*cnt + '1'*idx)
        
    return answer
