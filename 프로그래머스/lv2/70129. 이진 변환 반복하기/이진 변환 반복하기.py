def solution(s):
    i=0
    j=0
    while s!='1':
        j+=len(s)-s.count('1')
        s=s.replace('0','')
        s=bin(len(s))[2:]
        i+=1
    return [i,j]