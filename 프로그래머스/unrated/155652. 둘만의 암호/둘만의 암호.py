# 알파벳 리스트
from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''
    
    a=ascii_lowercase
    for x in skip:
        a=a.replace(x,'')
    
    for i in s:
        tmp=a[(a.index(i)+index) % len(a)]
        answer+=tmp
    
    return answer

