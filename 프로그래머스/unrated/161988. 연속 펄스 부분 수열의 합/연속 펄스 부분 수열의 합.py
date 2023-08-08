def solution(sequence):

    answer = 0
    sumlist = [0]
    for i in range(len(sequence)):
        sumlist.append(sumlist[-1]+(-1)**i*sequence[i])
    
    return abs(max(sumlist) - min(sumlist))