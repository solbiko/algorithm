def solution(s):
    i=0
    j=0
    while s!='1':
        cnt=len(s)
        s=s.replace('0','')
        cnt-=len(s)
        j+=cnt
        s=bin(len(s))[2:]
        i+=1
    return [i,j]