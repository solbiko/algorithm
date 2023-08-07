#  양쪽의 최솟값 중 하나라도 자신보다 클 경우 끝까지 남을 수 있음

def solution(a):
    if len(a)==1: return 1

    answer=2 # 양쪽 끝
    
    n=len(a)
    
    lm=[a[0]]
    rm=[a[-1]]

    for i in range(1, n):
        # 왼쪽 최솟값 저장
        if a[i]<lm[-1]:
            lm.append(a[i]) # 최솟값 추가
        else:
            lm.append(lm[-1]) # 기존값 추가
            
        # 오른쪽 최솟값 저장
        if a[-1-i]<rm[-1]: 
            rm.append(a[-1-i]) # 최솟값 추가
        else:
            rm.append(rm[-1])  # 기존값 추가
    rm.reverse()
          
    for i in range(1, n-1):
        if lm[i-1]>a[i] or rm[i+1]>a[i]:
            answer+=1
        
    return answer