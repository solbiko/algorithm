def str_to_int(time): # 시간 문자열 -> 숫자 변환
    h, m, s = time.split(':')
    return int(h)*60*60 +int(m)*60 + int(s)

def int_to_str(time): # 시간 숫자 -> 문자열 변환
    h = time//3600
    h ='0'+str(h) if h<10 else str(h)
    
    time=time%3600
    m = time // 60
    m = '0'+str(m) if m<10 else str(m)
    
    time = time%60
    s = '0'+str(time) if time<10 else str(time)
    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    answer = ''

    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    
    all_time = [0 for i in range(play_time + 1)]
    
    for l in logs:
        s,e=l.split('-')
        s=str_to_int(s)
        e=str_to_int(e)
        
        # 누적합
        all_time[s]+=1
        all_time[e]-=1
        
    # 구간별 시청자수 기록    
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]

    # 모든 구간 시청자수 누적 기록
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]

    most_view=0
    max_time=0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i-adv_time]:
                most_view = all_time[i] - all_time[i-adv_time]
                max_time=i-adv_time+1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time=i-adv_time+1
                
    return int_to_str(max_time)
    
    
    
    return answer