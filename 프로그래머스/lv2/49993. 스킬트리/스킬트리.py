def solution(skill, skill_trees):
    arr=[]
    for s in skill_trees:
        temp=''
        for x in s:
            if x in skill:
                temp+=x
            else:
                continue
        arr.append(temp)

    answer = 0
    for j in arr:
        if skill[:len(j)] == j:
            answer += 1
 
            
    return answer