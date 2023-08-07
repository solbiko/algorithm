def solution(enroll, referral, seller, amount):

    parent = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0]*len(enroll)))
    
    def distribute(target, money):
        if  money<10:
            answer[target]+=money
        elif parent[target]=='-':
            answer[target]+=money-money//10
        else:
            answer[target]+=money-money//10
            distribute(parent[target], money//10)

    for s,t in zip(seller, amount):
        distribute(s, t*100) # 이익금
     
    return list(answer.values())