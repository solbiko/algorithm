def solution(plans):
    answer = []
    wait = []

    plans.sort(key=lambda x: x[1])

    for p in plans:
        name, start, playtime=p
        h, m = map(int, start.split(":"))
        p[1] = time=h*60+m
        p[2] = int(p[2])
    
    for i,(n,s,p) in enumerate(plans):
        end = s + p # 종료시간

        if i == len(plans)-1:
            answer.append(n)
        else:
            next_start = plans[i+1][1] # 다음 시작 시간
            
            if end > next_start: # 안끝남
                p-=next_start-s
                wait.append([n, p])
                
            else: # 끝남
                answer.append(plans[i][0])
                
                left = next_start-end # 여유시간
                if wait and left > 0:
                    temp = wait[:]
                    for x in range(len(temp)-1, -1, -1): # 가장 최근에 멈춘 과제부터
                        name, playtime = temp[x]
                        if playtime <= left: # 여유시간 내에 오나료
                            wait.pop(x)
                            answer.append(name)
                            left -= playtime
                        else:
                            wait[x][1]-=left
                            break
    
    for item in wait[::-1]:
        answer.append(item[0])
        
    return answer