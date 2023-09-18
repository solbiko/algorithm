def solution(s):
    answer = []
    
    arr = s[2:-2].split("},{")
    arr.sort(key=lambda x : len(x))

    temp=set()
    for x in arr:
        xset = set(list(map(int, x.split(','))))
        answer = answer + list(set.difference(xset, temp))
        temp = xset

    
    return answer