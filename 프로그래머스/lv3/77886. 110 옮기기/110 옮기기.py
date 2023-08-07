def solution(s):
    answer = []
    
    # 110 개수 구하기
    for x in s: 
        
        # 110 개수 구하기
        stack=''
        cnt=0
        for i in x:
            if len(stack)>1 and i=='0' and stack[-2]=='1' and stack[-1]=='1':
                stack = stack[:-2]
                cnt+=1
            else:
                stack+=i
        
        # print(stack)
        idx = stack.find("111")  # 111 찾기
        if idx == -1:  # 0뒤에 110 반복해 붙이기
            idx = stack.rfind('0')
            stack = stack[:idx+1] + "110"*cnt + stack[idx+1:]
        else: # 111앞에 110 반복해 붙이기
            stack = stack[:idx] + "110"*cnt + stack[idx:]
        answer.append(stack)
        
    return answer 