def solution(storey):
    answer = 0

    while storey:
        r = storey % 10
        print(storey,r)

        if r > 5:# 6 ~ 9
            answer += (10-r)
            storey += 10
        
        else:
            if r==5 and (storey // 10) % 10 > 4:
                storey += 10
            answer+=r
            
        storey //= 10

    return answer