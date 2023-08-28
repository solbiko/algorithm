def solution(lottos, win_nums):
    
    c = 0
    for i in lottos:
        if i in win_nums:
            c+=1
  
    rank=[6,6,5,4,3,2,1]
    return rank[lottos.count(0)+c],rank[c]
