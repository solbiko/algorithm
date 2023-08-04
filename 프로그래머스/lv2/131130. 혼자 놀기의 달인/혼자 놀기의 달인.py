def solution(cards):
    answer = []
    
    for x in range(len(cards)):
        temp = []
        while cards[x] not in temp:
            temp.append(cards[x])
            x = cards[x]-1
            
        answer.append([] if sorted(temp) in answer else sorted(temp))
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])