def solution(n):
    answer = 0
    # for i in range(1,n+1):
    #     temp=0
    #     for j in range(i,n+1):
    #         temp+=j
    #         if temp==n:
    #             answer+=1
    #         elif temp>n:
    #             break

    """
    n의 홀수인 약수의 개수
    
    1) 약수가 1
        1로 인해 15는 연속하는 하나의 자연수, 15
    2) 약수가 3
        3으로 인해 15는 5+5+5 의 합으로 표현되는 것을 알 수 있고 약간의 조작을 통해 4+5+6 (연속하는 자연수)
    3) 약수가 5
        5도 마찬가지로 3+3+3+3+3 즉, 1+2+3+4+5
    4) 약수가 15
        모든 홀수 2n+1는 n 과 n+1, 연속하는 두 수의 합으로 표현 할 수 있으므로 7+8
    """
    
    result=[]
    for i in range(1,n+1,2):
        if n % i == 0:
            result.append(i)
    answer=len(result)
    
    return answer