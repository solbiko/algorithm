from collections import Counter
def solution(clothes):
    dict={}
    for x,type in clothes:
        if type in dict:
            dict[type].append(x)
        else:
            dict[type]=[x]
    
    answer = 1
    for type in dict:
        answer*=len(dict[type])+1 # 입지않는 경우의 수 포함
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외
    return answer - 1