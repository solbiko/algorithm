def solution(progresses, speeds):
    answer = []

    cnt = 0
    day = 0
    while len(progresses)>0:
        if progresses[0] + day*speeds[0] >= 100: # 완료

            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
            
        else: # 미완
            if cnt>0: # 지금까지 완료한 기능 배포하고 초기화 
                answer.append(cnt)
                cnt=0
            day+=1

    answer.append(cnt)
    return answer