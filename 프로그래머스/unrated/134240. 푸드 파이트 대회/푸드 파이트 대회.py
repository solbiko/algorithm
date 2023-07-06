def solution(food):
    answer = ''
    for i in range(len(food)):
        for j in range(1,food[i]//2+1):
            answer+=str(i)
    answer+='0'+answer[::-1]
    return answer