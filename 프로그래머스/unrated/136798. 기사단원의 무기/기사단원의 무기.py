def solution(number, limit, power):
    answer = 0
    
    for x in range(1,number+1):
        cnt=0
        for i in range(1, int(x**(1/2))+1):
            if x%i==0:
                cnt+=1
                if i**2 != x: #제곱이 되는 약수 중복 방지
                    cnt+=1
        if cnt>limit:
            cnt=power
        answer+=cnt
    return answer