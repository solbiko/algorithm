# 연속 펄스 부분 수열의 합 중 가장 큰 것
def solution(sequence):
    n=len(sequence)
    
    temp1=[sequence[i]*(-1)**(i+1) for i in range(n)] # -1 1 펄스 곱한 리스트
    temp2=[sequence[i]*(-1)**i for i in range(n)] # 1 -1 펄스 곱한 리스트
    
    dp1=[0]*n
    dp1[0]=temp1[0]
    
    dp2=[0]*n
    dp2[0]=temp2[0]

    for i in range(1, n):
        dp1[i] = max(dp1[i-1]+temp1[i], temp1[i])
        dp2[i] = max(dp2[i-1]+temp2[i], temp2[i])
    
    return max(max(dp1), max(dp2))


    