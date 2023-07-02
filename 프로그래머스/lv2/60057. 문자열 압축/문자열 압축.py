def solution(s):
    answer=len(s)

    for i in range(1, len(s)//2+1):
        res=""

        prev=s[0:i] # 앞에서부터 i 문자열 추출
        cnt=1
        
        for j in range(i, len(s), i): # i만큼 증가시키며 이전 문자열과 비교
            if prev==s[j:j+i]:
                cnt+=1  # 이전 상태와 동일하면 증가

            else: # 다른 문자열이 나왔다면, 압축 불가
                res += str(cnt)+prev if cnt>=2 else prev
                # 초기화
                prev=s[j:j+i] 
                cnt=1

        # 남아있는 문자열
        res+=str(cnt)+prev if cnt>=2 else prev
        answer=min(answer, len(res))
        
    return answer