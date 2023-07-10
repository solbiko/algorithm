def solution(s):
    i=0
    j=0
    while s!='1':
        num = s.count('1')
        j+=len(s)-num
        s=bin(num)[2:]
        i+=1
    return [i,j]