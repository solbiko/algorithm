def solution(picks, minerals):
    answer = 0

    if len(minerals)>sum(picks)*5:
        minerals=minerals[:sum(picks)*5]

    # 광물 5개씩 끊은 리스트
    mlist=[[0,0,0] for _ in range((len(minerals))//5+1)]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            mlist[i//5][0]+=1
        elif minerals[i]=='iron':
            mlist[i//5][1]+=1
        elif minerals[i]=='stone':
            mlist[i//5][2]+=1

    mlist.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    
    for x in mlist:
        dia,iron,stone = x
        for j in range(len(picks)):
            if picks[j]>0 and j==0: # 다이아몬드 곡괭이
                picks[j]-=1
                answer+=dia+iron+stone
                break
            elif picks[j]>0 and j==1: # 철 곡괭이
                picks[j]-=1
                answer+=dia*5+iron+stone
                break
            elif picks[j]>0 and j==2: # 돌 곡괭이
                picks[j]-=1
                answer+=dia*25+iron*5+stone
                break
    return answer